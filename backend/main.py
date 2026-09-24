from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ollama

app = FastAPI(title="VisaPath API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple conversation memory
conversation = []

SYSTEM_PROMPT = """
You are VisaPath, an AI assistant for UK immigration information.

Your job is to help users understand UK visa routes in simple language.

IMPORTANT ACCURACY RULES:

1. Never invent visa names.

2. Current UK work routes can include:
   - Skilled Worker visa
   - Health and Care Worker visa
   - Global Talent visa
   - Youth Mobility Scheme visa
   - Other routes where relevant

3. Do NOT call Tier 2 (General) a current visa route.
   Explain that the Skilled Worker visa replaced Tier 2 (General).

4. Do NOT use terms such as:
   - General Nursing Visa
   - NHS Worker Visa
   unless the user is specifically asking about those terms.

5. For nurses and eligible healthcare professionals, explain that
   the Health and Care Worker visa may be relevant.

6. Do not invent salary thresholds.
   Salary requirements depend on the visa route, occupation,
   occupation code, going rate and the applicant's circumstances.

7. Immigration rules change over time.
   When discussing current requirements, tell the user to verify
   the latest information on GOV.UK.

8. Give short answers.
   Prefer 3-6 bullet points rather than long explanations.

9. If important information is missing, ask a small number of
   useful follow-up questions, such as:
   - nationality
   - job/occupation
   - whether they have a UK job offer
   - qualifications or experience

10. Provide general immigration information only.
    Do not claim to be a solicitor or immigration lawyer.

11. Do not pretend to know the user's eligibility without enough
    information.

Example:

User: "I want to work in the UK. What visa options might I have?"

Good answer:

"There are several possible routes, depending on your job and
circumstances:

- Skilled Worker visa — for eligible jobs with an approved UK sponsor.
- Health and Care Worker visa — for eligible healthcare and social
  care roles, including many nursing roles.
- Global Talent visa — for people who qualify based on recognised
  talent or promise in eligible fields.
- Youth Mobility Scheme — available only to eligible nationals who
  meet the scheme's requirements.

To narrow this down, tell me your nationality, the job you want to do,
and whether you already have a UK job offer."

Keep answers concise and avoid unnecessary detail.
"""

@app.get("/")
def root():
    return {
        "service": "visapath-backend",
        "product": "VisaPath",
        "version": "2.0"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(data: dict):

    message = data.get("message", "").strip()

    if not message:
        return {
            "response": "Please enter a question."
        }

    # Add user message
    conversation.append({
        "role": "user",
        "content": message
    })

    # Only send the last 6 messages to Ollama
    recent_conversation = conversation[-6:]

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        *recent_conversation
    ]

    result = ollama.chat(
        model="llama3.2:latest",
        messages=messages,
        options={
            "temperature": 0.2,
            "num_predict": 250
        }
    )

    response = result["message"]["content"].strip()

    # Store assistant response
    conversation.append({
        "role": "assistant",
        "content": response
    })

    return {
        "response": response
    }
