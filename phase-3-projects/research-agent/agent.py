"""Research Assistant Agent — Phase 3, Milestone 1.

A LangGraph agent that answers questions using real tools:
  - wikipedia_search: look up factual info on Wikipedia (given — API plumbing)
  - calculator:       evaluate arithmetic safely (YOU write this)

Run from the terminal:
    uv run python phase-3-projects/research-agent/agent.py "How tall is Mount Everest in feet?"
"""

import sys
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")

_WIKI_HEADERS = {"User-Agent": "ai-learning-research-agent/0.1"}


# --- Tool 1: Wikipedia search (GIVEN — this is API plumbing, like the embed() helper) ---
@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia and return a short factual summary for the best-matching article."""
    search = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={"action": "query", "list": "search", "srsearch": query, "format": "json", "srlimit": 1},
        headers=_WIKI_HEADERS, timeout=10,
    ).json()
    hits = search.get("query", {}).get("search", [])
    if not hits:
        return f"No Wikipedia article found for '{query}'."
    title = hits[0]["title"]
    summary = requests.get(
        f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}",
        headers=_WIKI_HEADERS, timeout=10,
    ).json()
    return f"{title}: {summary.get('extract', 'No summary available.')}"


# --- Tool 2: Calculator (YOU write this) ---
# TODO: implement a `calculator` tool that evaluates a simple arithmetic expression
#       (e.g. "8848 * 3.281") and returns the result.
# SECURITY NOTE: do NOT use bare eval() — this runs on user input in a deployed app.
#   Use a safe approach (e.g. the `ast` module to parse + evaluate only arithmetic nodes,
#   or a restricted evaluator). Decorate it with @tool and give it a clear docstring.


# --- Build the agent (YOU write this — it's your P2-A7 graph) ---
def build_agent():
    """Return a compiled LangGraph agent with the two tools wired in."""
    tools = [wikipedia_search]  # TODO: add your calculator once written
    # TODO: bind tools to the llm; build a StateGraph(MessagesState) with an `agent`
    #       node and a ToolNode; wire START -> agent, conditional edge via tools_condition,
    #       and tools -> agent. Compile and return it.
    raise NotImplementedError("build_agent not implemented yet")


def run(question: str) -> str:
    """Run the agent on one question and return the final text answer."""
    agent = build_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "What is the capital of Australia, and what is its population times 2?"
    print(f"Q: {q}\n")
    print("A:", run(q))
