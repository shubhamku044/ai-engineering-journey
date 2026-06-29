# AI Engineering Journey

My self-paced path from full-stack development into **applied AI / AI-engineering** — LLMs, RAG, agents, LangChain/LangGraph. This repo is a public learning log: every assignment, with code and notes, organized by phase and week. Mentored daily, reviewed like code.

> Starting point: ~1 year full-stack (React/Next.js + Python/Django/Celery/Redis/Elasticsearch). Goal: ship real applied-AI systems.

## Roadmap

| Phase | Focus |
|-------|-------|
| 1 | Python for data (NumPy/Pandas) + math *intuition* |
| 2 | ML fundamentals (supervised learning, overfitting, metrics) |
| 3 | Deep learning basics (PyTorch, embeddings) |
| 4 | **Applied AI / LLMs** (prompting, RAG, vector DBs, tool calling, LangChain, LangGraph, agents, evals) ← focus |
| 5 | Build & ship 2–3 deployed portfolio projects |
| 6 | Specialize |

## Setup (uv)

```bash
uv sync                       # install deps into .venv from the lockfile
uv run jupyter notebook       # launch Jupyter (no manual activate needed)
uv add <package>              # add a new dependency
```

No `source .venv/bin/activate` needed — `uv run <cmd>` handles the environment.

## Structure

```
phase-1-python-for-data/
  week-01/
    a1-numpy/            # vectorized NumPy ops
    a2-pandas-titanic/   # Titanic EDA
    a3-mini-project/     # charts + writeup
```

Each assignment folder holds a notebook (`.ipynb`) or script plus a short `NOTES.md` explaining the approach and what I learned.

## Progress log

| Date | Assignment | Status | Score |
|------|-----------|--------|-------|
| 2026-06-29 | Phase 1 · Week 1 · A1 NumPy | in progress | — |

## Resources

3Blue1Brown · Andrew Ng ML Specialization · Kaggle Learn · fast.ai · DeepLearning.AI short courses · Hugging Face · LangChain/LangGraph docs
