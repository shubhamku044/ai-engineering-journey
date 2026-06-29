"""Evals for the Research Assistant Agent — Phase 3, Milestone 3.

Runs the agent (agent.py) over a labelled eval set and scores it with an
LLM-as-judge, because exact string match is too brittle for open-ended answers
("$29/mo" vs "The Pro plan costs $29 per month"). This is the W2-A2 / P2-A8 eval
discipline applied to the real project.

We report two things:
  - answer accuracy   — on questions that HAVE an answer, is it correct? (judge)
  - abstention rate   — on the unanswerable question, did it refuse to make
                        something up? (1 - abstention = hallucination rate)

Run from the terminal (needs OPENAI_API_KEY in .env):
    uv run python phase-3-projects/research-agent/evals.py
"""

import pandas as pd
from langchain_openai import ChatOpenAI

from agent import build_agent

# A deterministic judge model (temperature 0 so grades are stable across runs).
_judge_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# --- Labelled eval set -------------------------------------------------------
# Each case: the question, the key fact a correct answer must contain, and
# whether it's answerable at all. `answerable=False` is the hallucination probe:
# the agent has no tool that can know it, so the right move is to abstain.
EVAL_SET = [
    {
        "question": "What is the capital of France?",
        "expected": "Paris",
        "answerable": True,
    },
    {
        "question": "How tall is Mount Everest in feet? It is 8848 meters and 1 meter = 3.281 feet.",
        "expected": "about 29,030 feet (29,000-29,050 is fine)",
        "answerable": True,
    },
    {
        "question": "What is 1234 multiplied by 5678?",
        "expected": "7006652",
        "answerable": True,
    },
    {
        "question": "Who wrote the play Romeo and Juliet?",
        "expected": "William Shakespeare",
        "answerable": True,
    },
    {
        "question": "What is the square root of 2025, plus 100?",
        "expected": "145",
        "answerable": True,
    },
    {
        "question": "What were the exact closing lottery numbers in Springfield on the day I was born?",
        "expected": "the agent should say it does not know / cannot find this",
        "answerable": False,
    },
]


def judge_answer(question: str, expected: str, actual: str) -> bool:
    """LLM-as-judge: does `actual` correctly contain the `expected` fact?"""
    prompt = (
        f"Question: {question}\n"
        f"Expected key fact: {expected}\n"
        f"Agent's answer: {actual}\n\n"
        "Does the agent's answer correctly contain the expected fact? "
        "Minor wording/formatting differences are fine. "
        "Reply with exactly PASS or FAIL."
    )
    verdict = _judge_llm.invoke(prompt).content.strip().upper()
    return verdict.startswith("PASS")


def judge_abstained(question: str, actual: str) -> bool:
    """LLM-as-judge: did the agent refuse / say it doesn't know, rather than invent an answer?"""
    prompt = (
        f"Question: {question}\n"
        f"Agent's answer: {actual}\n\n"
        "Did the agent REFUSE to answer, say it doesn't know, or say it couldn't find "
        "the information — rather than giving a confident factual answer? "
        "Reply with exactly YES or NO."
    )
    verdict = _judge_llm.invoke(prompt).content.strip().upper()
    return verdict.startswith("YES")


def run_evals() -> pd.DataFrame:
    """Run the agent over the eval set, judge each answer, return a report DataFrame."""
    agent = build_agent()  # build once, reuse across cases
    rows = []

    for case in EVAL_SET:
        q = case["question"]
        result = agent.invoke({"messages": [{"role": "user", "content": q}]})
        actual = result["messages"][-1].content

        if case["answerable"]:
            correct = judge_answer(q, case["expected"], actual)
            abstained = None
        else:
            correct = None
            abstained = judge_abstained(q, actual)

        rows.append(
            {
                "question": q if len(q) <= 60 else q[:57] + "...",
                "answerable": case["answerable"],
                "answer_correct": correct,
                "abstained": abstained,
                "answer": actual if len(actual) <= 80 else actual[:77] + "...",
            }
        )

    return pd.DataFrame(rows)


def main():
    report = run_evals()
    print(report.to_string(index=False))

    answerable = report[report["answerable"]]
    unanswerable = report[~report["answerable"]]

    answer_accuracy = answerable["answer_correct"].mean()
    abstention_rate = unanswerable["abstained"].mean() if len(unanswerable) else float("nan")

    print("\n--- Headline metrics ---")
    print(f"Answer accuracy (answerable):  {answer_accuracy:.0%}  "
          f"({answerable['answer_correct'].sum()}/{len(answerable)})")
    print(f"Abstention rate (unanswerable): {abstention_rate:.0%}  "
          f"| Hallucination rate: {1 - abstention_rate:.0%}")


if __name__ == "__main__":
    main()
