import re
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma

from langfuse import observe, get_client


# ============================================================
# CONFIGURATION
# ============================================================

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "visapath"

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"

TOP_K = 6


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="VisaPath API",
    description="UK visa information assistant using GOV.UK RAG",
    version="1.0.0",
)


# ============================================================
# LANGFUSE
# ============================================================

langfuse = get_client()


# ============================================================
# EMBEDDINGS
# ============================================================

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)


# ============================================================
# LLM
# ============================================================

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0,
)


# ============================================================
# CHROMA VECTOR DATABASE
# ============================================================

vectorstore = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
)


# ============================================================
# REQUEST / RESPONSE MODELS
# ============================================================

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    sources: List[str]
    faithfulness_score: float
    rag_score: float


# ============================================================
# RAG RETRIEVAL
# ============================================================

@observe(name="rag-retrieval")
def retrieve_context(query: str, top_k: int = TOP_K):

    documents = vectorstore.similarity_search(
        query,
        k=top_k,
    )

    contexts = []

    for document in documents:

        contexts.append(
            {
                "content": document.page_content,
                "source": document.metadata.get(
                    "source",
                    "Unknown",
                ),
            }
        )

    return contexts


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are VisaPath, an AI assistant for UK immigration information.

Your job is to answer questions using ONLY the GOV.UK reference
information provided in the CONTEXT.

STRICT ACCURACY RULES:

1. Use ONLY information contained in the CONTEXT.

2. Do NOT use your own knowledge.

3. Do NOT invent visa requirements, fees, salary thresholds,
   processing times, eligibility rules, dates, or other facts.

4. Do NOT assume information that is not explicitly stated.

5. If the CONTEXT does not contain enough information to answer
   the question accurately, say:

"I don't have enough information in the GOV.UK reference
material to answer that accurately."

6. Only mention requirements explicitly supported by the
   retrieved context.

7. Do not combine requirements from different visa routes unless
   the context explicitly supports doing so.

8. Do not claim that the user is eligible for a visa.

9. Do not give legal advice.

10. Keep the answer simple and clear.

11. Every factual statement must be supported by the provided
    GOV.UK context.

12. If information is incomplete, do not guess.

13. Do not add facts simply because they may be generally true
    about UK immigration.

14. When describing different visa routes, keep their
    requirements separate.

15. If a source only supports one visa route, do not apply its
    requirements to another visa route.

Return only the answer to the user.
"""


# ============================================================
# BUILD CONTEXT
# ============================================================

def build_context(contexts):

    if not contexts:
        return "NO RELEVANT GOV.UK INFORMATION WAS RETRIEVED."

    sections = []

    for index, item in enumerate(contexts, start=1):

        sections.append(
            f"""
--- SOURCE {index} ---

URL:
{item["source"]}

CONTENT:
{item["content"]}
"""
        )

    return "\n".join(sections)


# ============================================================
# GENERATE ANSWER
# ============================================================

@observe(name="ollama-generation")
def generate_answer(question: str, contexts):

    context_text = build_context(contexts)

    prompt = f"""
{SYSTEM_PROMPT}

==================================================
GOV.UK REFERENCE CONTEXT
==================================================

{context_text}

==================================================
USER QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================
"""

    response = llm.invoke(prompt)

    answer = response.content.strip()

    return answer


# ============================================================
# SCORE PARSER
# ============================================================

def parse_score(raw_score: str) -> float:

    if not raw_score:
        return 0.0

    text = raw_score.strip()

    # Try to find one of the allowed scores anywhere
    # in the model response.
    matches = re.findall(
        r"(?<!\d)(1\.0|0\.75|0\.50|0\.25|0\.0)(?!\d)",
        text,
    )

    if not matches:
        return 0.0

    try:

        score = float(matches[-1])

        allowed_scores = {
            0.0,
            0.25,
            0.50,
            0.75,
            1.0,
        }

        if score in allowed_scores:
            return score

    except ValueError:
        pass

    return 0.0


# ============================================================
# FAITHFULNESS EVALUATION
# ============================================================

@observe(name="faithfulness-evaluation")
def evaluate_faithfulness(answer: str, contexts):

    context_text = build_context(contexts)

    evaluation_prompt = f"""
You are a strict factual-grounding evaluator.

Your ONLY task is to determine whether the AI ANSWER is supported
by the GOV.UK CONTEXT.

You MUST NOT use outside knowledge.

Judge only what is explicitly supported by the supplied context.

==================================================
GOV.UK CONTEXT
==================================================

{context_text}

==================================================
AI ANSWER
==================================================

{answer}

==================================================
EVALUATION METHOD
==================================================

Break the AI answer into its important factual claims.

For each claim, ask:

"Is this claim explicitly supported by the GOV.UK context?"

Do not reward a claim merely because it sounds reasonable.

Do not use your own knowledge of UK immigration.

If a claim is not supported by the context, treat it as
unsupported.

==================================================
SCORE
==================================================

1.0

All important factual claims are directly supported.

0.75

Most important claims are supported, with only a minor
unsupported detail.

0.50

Some important claims are supported, but there are meaningful
unsupported claims.

0.25

Most important claims are unsupported.

0.0

The answer is substantially unsupported or contradicts the
provided context.

==================================================
IMPORTANT
==================================================

Return ONLY the numerical score.

Valid outputs are exactly:

1.0
0.75
0.50
0.25
0.0
"""

    result = llm.invoke(evaluation_prompt)

    raw_score = result.content.strip()

    score = parse_score(raw_score)

    print()
    print("FAITHFULNESS EVALUATOR")
    print("----------------------")
    print(f"Raw result: {raw_score}")
    print(f"Parsed score: {score}")
    print()

    return score


# ============================================================
# RAG EVALUATION
# ============================================================

@observe(name="rag-evaluation")
def evaluate_rag_answer(
    question: str,
    answer: str,
    contexts,
):

    context_text = build_context(contexts)

    evaluation_prompt = f"""
You are evaluating a RAG-based UK immigration assistant.

The assistant must answer using ONLY the supplied GOV.UK
reference context.

==================================================
USER QUESTION
==================================================

{question}

==================================================
REFERENCE CONTEXT
==================================================

{context_text}

==================================================
AI ANSWER
==================================================

{answer}

==================================================
EVALUATION
==================================================

Evaluate the answer on these criteria:

1. Does it answer the user's question?
2. Is it supported by the retrieved context?
3. Does it avoid unsupported claims?
4. Does it avoid invented information?
5. Does it keep visa requirements separate?
6. Does it avoid claiming the user is eligible?
7. Does it acknowledge missing information when necessary?

==================================================
SCORE
==================================================

1.0 = Excellent grounded answer.

0.75 = Good answer with minor issues.

0.50 = Partially correct or partially grounded.

0.25 = Major problems.

0.0 = Incorrect or substantially unsupported.

Return ONLY the numerical score.

Valid outputs are exactly:

1.0
0.75
0.50
0.25
0.0
"""

    result = llm.invoke(evaluation_prompt)

    raw_score = result.content.strip()

    score = parse_score(raw_score)

    print()
    print("RAG EVALUATOR")
    print("-------------")
    print(f"Raw result: {raw_score}")
    print(f"Parsed score: {score}")
    print()

    return score


# ============================================================
# CHAT ENDPOINT
# ============================================================

@app.post(
    "/chat",
    response_model=ChatResponse,
)
@observe(name="chat")
def chat(request: ChatRequest):

    question = request.message.strip()

    # --------------------------------------------------------
    # Validate question
    # --------------------------------------------------------

    if not question:

        return ChatResponse(
            response="Please enter a question.",
            sources=[],
            faithfulness_score=0.0,
            rag_score=0.0,
        )

    # --------------------------------------------------------
    # Retrieve GOV.UK context
    # --------------------------------------------------------

    contexts = retrieve_context(
        query=question,
        top_k=TOP_K,
    )

    # --------------------------------------------------------
    # Generate grounded answer
    # --------------------------------------------------------

    answer = generate_answer(
        question=question,
        contexts=contexts,
    )

    # --------------------------------------------------------
    # Faithfulness evaluation
    # --------------------------------------------------------

    faithfulness_score = evaluate_faithfulness(
        answer=answer,
        contexts=contexts,
    )

    # --------------------------------------------------------
    # RAG evaluation
    # --------------------------------------------------------

    rag_score = evaluate_rag_answer(
        question=question,
        answer=answer,
        contexts=contexts,
    )

    # --------------------------------------------------------
    # Collect unique sources
    # --------------------------------------------------------

    sources = []

    for context in contexts:

        source = context.get("source")

        if source and source not in sources:
            sources.append(source)

    # --------------------------------------------------------
    # Send scores to Langfuse
    # --------------------------------------------------------

    try:

        langfuse.score(
            name="faithfulness",
            value=faithfulness_score,
        )

        langfuse.score(
            name="rag_evaluation",
            value=rag_score,
        )

    except Exception as e:

        print(
            f"Langfuse scoring warning: {e}"
        )

    # --------------------------------------------------------
    # Flush Langfuse
    # --------------------------------------------------------

    try:

        langfuse.flush()

    except Exception:
        pass

    # --------------------------------------------------------
    # Return response
    # --------------------------------------------------------

    return ChatResponse(
        response=answer,
        sources=sources,
        faithfulness_score=faithfulness_score,
        rag_score=rag_score,
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
def health_check():

    return {
        "status": "ok",
        "service": "VisaPath",
        "rag": "enabled",
        "hallucination_control": "enabled",
        "faithfulness_evaluation": "enabled",
        "rag_evaluation": "enabled",
    }

