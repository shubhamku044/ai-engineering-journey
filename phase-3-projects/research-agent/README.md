# Research Assistant Agent

A tool-using LLM agent (LangGraph + OpenAI) that answers questions by searching Wikipedia and doing calculations — then citing what it used. Phase 3 portfolio project.

## Status
- [ ] **M1 — Agent core** (`agent.py`): LangGraph agent + tools, runnable from terminal
- [ ] **M2 — Web UI** (`app.py`): Streamlit chat interface
- [ ] **M3 — Evals** (`evals.py`): eval set + LLM-as-judge
- [ ] **M4 — Deploy**: live public URL + this README with architecture & screenshots

## Tools
- `wikipedia_search` — factual lookups via the Wikipedia REST API (free, no key)
- `calculator` — safe arithmetic

## Run (local)
```bash
# from repo root; needs OPENAI_API_KEY in .env
uv run python phase-3-projects/research-agent/agent.py "How tall is Mount Everest in feet?"
```

## How it works
A LangGraph agent loop: the model decides when to call a tool, the tool runs, the result feeds back, and it repeats until it has a final answer. (Same loop built by hand in `phase-2-applied-ai-llms/p2-a6` and with LangGraph in `p2-a7`.)
