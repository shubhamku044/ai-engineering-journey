"""Research Assistant Agent — Phase 3, Milestone 1.

A LangGraph agent that answers questions using real tools:
  - wikipedia_search: look up factual info on Wikipedia (given — API plumbing)
  - calculator:       evaluate arithmetic safely (YOU write this)

Run from the terminal:
    uv run python phase-3-projects/research-agent/agent.py "How tall is Mount Everest in feet?"
"""

import ast
import operator
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


# --- Tool 2: Calculator (safe arithmetic via the `ast` module) ---
# We parse the expression into an AST and walk only the nodes that represent
# arithmetic. Anything else (function calls, names, attribute access, etc.) is
# rejected — so unlike bare eval(), there is no way to run arbitrary code.
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _safe_eval(node):
    """Recursively evaluate an arithmetic-only AST node, or raise ValueError."""
    if isinstance(node, ast.Constant):  # numbers only — no strings/bytes/etc.
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("only numeric literals are allowed")
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        return _BIN_OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return _UNARY_OPS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("unsupported expression")


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression and return the result.

    Supports + - * / // % ** , parentheses, and decimals (e.g. "8848 * 3.281").
    Use this for any numeric computation instead of doing the math yourself.
    """
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree.body)
    except ZeroDivisionError:
        return "Error: division by zero."
    except (ValueError, SyntaxError, TypeError):
        return f"Error: '{expression}' is not a valid arithmetic expression."
    return str(result)


# --- Build the agent (YOU write this — it's your P2-A7 graph) ---
def build_agent():
    """Return a compiled LangGraph agent with the two tools wired in."""
    tools = [wikipedia_search, calculator]
    bound = llm.bind_tools(tools)

    def agent_node(state):
        return {"messages": [bound.invoke(state["messages"])]}

    graph = StateGraph(MessagesState)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", tools_condition)  # tool calls -> 'tools', else END
    graph.add_edge("tools", "agent")  # loop back after running tools
    return graph.compile()


def run(question: str) -> str:
    """Run the agent on one question and return the final text answer."""
    agent = build_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "What is the capital of Australia, and what is its population times 2?"
    print(f"Q: {q}\n")
    print("A:", run(q))
