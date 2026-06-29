# Research Assistant Agent

A tool-using LLM agent (LangGraph + OpenAI) that answers questions by searching Wikipedia and doing calculations — then citing what it used. Phase 3 portfolio project.

## Status
- [x] **M1 — Agent core** (`agent.py`): LangGraph agent + tools, runnable from terminal
- [ ] **M2 — Web UI**: *skipped by choice* — agent runs as a CLI/module; would deploy as an API
- [x] **M3 — Evals** (`evals.py`): eval set + LLM-as-judge
- [ ] **M4 — Deploy**: *process documented below* (not deployed)

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

## Deployment (process, not yet deployed)
The agent is a stateless Python function (`run(question) -> str`). To ship it as a service:

1. **Expose an HTTP endpoint** — wrap `run()` in a thin FastAPI app (`POST /ask {"question": ...}`). No UI needed; it's a backend any frontend can call.
2. **Secrets** — `OPENAI_API_KEY` is set as a platform **environment variable / secret**, never committed. `.env` stays git-ignored and is for local dev only.
3. **Dependencies** — the platform installs from `pyproject.toml` + `uv.lock` (reproducible), or `uv export > requirements.txt` for platforms that expect pip.
4. **Host** — containerize (Dockerfile) and deploy to Render / Railway / Fly.io / Cloud Run, or a serverless function. Pin Python 3.12.
5. **LLM-specific runtime concerns:**
   - **Timeouts** — an agent loop makes several LLM + tool calls; a request can take 10–60s. Set generous server/client timeouts.
   - **Cost & safety caps** — keep a `max_steps` recursion limit so a misbehaving loop can't burn tokens indefinitely.
   - **Statelessness** — each request is independent. For multi-turn memory, add a LangGraph checkpointer keyed by a session/thread id.
   - **Observability** — wire up tracing (e.g. LangSmith) to see each tool call and catch failures in production.
   - **Rate limits / retries** — handle provider 429s with backoff.
