import requests
import statistics
import time


API_URL = "http://127.0.0.1:8000/chat"


QUESTIONS = [
    "What is a Skilled Worker visa?",
    "What are the main requirements for a Skilled Worker visa?",
    "Do I need a confirmed job offer for a Skilled Worker visa?",
    "What is a Certificate of Sponsorship?",
    "How long can a Skilled Worker visa last?",
    "Can I extend a Skilled Worker visa?",
    "What English language requirement applies to a Skilled Worker visa?",
    "What is a Health and Care Worker visa?",
    "Do I need a confirmed job offer for a Health and Care Worker visa?",
    "How long can a Health and Care Worker visa last?",
    "Can a Health and Care Worker visa be extended?",
    "Can someone on a Health and Care Worker visa eventually apply to settle?",
    "What is the Youth Mobility Scheme visa?",
    "How long can you stay under the Youth Mobility Scheme?",
    "What can you do while on the Youth Mobility Scheme visa?",
    "Can you work while on the Youth Mobility Scheme visa?",
    "What is the Global Talent visa?",
    "How much does a Skilled Worker visa cost?",
    "Can I change my employer while on a Skilled Worker visa?",
    "What UK visa should I get if I have a job offer?",
]


def ask_question(question):
    response = requests.post(
        API_URL,
        json={"message": question},
        timeout=180,
    )

    response.raise_for_status()

    return response.json()


def main():
    print()
    print("=" * 70)
    print("VisaPath - RAG Evaluation")
    print("=" * 70)
    print()

    faithfulness_scores = []
    rag_scores = []

    results = []

    for number, question in enumerate(QUESTIONS, start=1):

        print(f"[{number}/20] {question}")

        try:
            result = ask_question(question)

            faithfulness = float(
                result.get("faithfulness_score", 0.0)
            )

            rag_score = float(
                result.get("rag_score", 0.0)
            )

            sources = result.get("sources", [])

            faithfulness_scores.append(faithfulness)
            rag_scores.append(rag_score)

            results.append(
                {
                    "question": question,
                    "faithfulness": faithfulness,
                    "rag_score": rag_score,
                    "sources": sources,
                }
            )

            print(
                f"    Faithfulness: {faithfulness:.2f}"
            )

            print(
                f"    RAG score:    {rag_score:.2f}"
            )

            print(
                f"    Sources:      {len(sources)}"
            )

        except Exception as e:

            print(
                f"    ERROR: {e}"
            )

            results.append(
                {
                    "question": question,
                    "faithfulness": 0.0,
                    "rag_score": 0.0,
                    "sources": [],
                }
            )

            faithfulness_scores.append(0.0)
            rag_scores.append(0.0)

        print()

        # Small pause so the local server is not hammered.
        time.sleep(0.5)

    print()
    print("=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    print()

    if faithfulness_scores:
        average_faithfulness = statistics.mean(
            faithfulness_scores
        )
    else:
        average_faithfulness = 0.0

    if rag_scores:
        average_rag = statistics.mean(
            rag_scores
        )
    else:
        average_rag = 0.0

    perfect_faithfulness = sum(
        score == 1.0
        for score in faithfulness_scores
    )

    perfect_rag = sum(
        score == 1.0
        for score in rag_scores
    )

    print(
        f"Questions evaluated:     {len(QUESTIONS)}"
    )

    print(
        f"Average faithfulness:     {average_faithfulness:.2f}"
    )

    print(
        f"Average RAG score:        {average_rag:.2f}"
    )

    print(
        f"Faithfulness 1.0:         "
        f"{perfect_faithfulness}/{len(QUESTIONS)}"
    )

    print(
        f"RAG score 1.0:            "
        f"{perfect_rag}/{len(QUESTIONS)}"
    )

    print()

    print("=" * 70)
    print("QUESTION RESULTS")
    print("=" * 70)
    print()

    for number, result in enumerate(results, start=1):

        print(
            f"{number:02d}. {result['question']}"
        )

        print(
            f"    Faithfulness: "
            f"{result['faithfulness']:.2f}"
        )

        print(
            f"    RAG:          "
            f"{result['rag_score']:.2f}"
        )

        print(
            f"    Sources:      "
            f"{len(result['sources'])}"
        )

        print()

    print("=" * 70)
    print("Evaluation complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()