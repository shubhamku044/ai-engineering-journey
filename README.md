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
| 2026-06-29 | Phase 1 · Week 1 · A1 NumPy (vectorized ops + broadcasting) | ✅ done | 8.5/10 |
| 2026-06-29 | Phase 1 · Week 1 · A2 Pandas EDA (Titanic) | ✅ done | 8/10 |
| 2026-06-29 | Phase 1 · Week 1 · A3 Mini project (charts + writeup) | 🔜 in progress | — |

## Resources

Curated, free, and watch-in-order per phase. **Bold = start here.**

### Phase 1 — Python for data + math intuition (now)
- **[Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas)** — short, hands-on, mirrors what you're doing.
- [Corey Schafer — Pandas tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — the canonical pandas walkthrough on YouTube.
- [pandas docs — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [NumPy — broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- **[3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)** — intuition only, no grinding proofs. Watch ~1 video/day alongside assignments.

### Phase 2 — ML fundamentals
- **[Andrew Ng — Machine Learning Specialization (Coursera, audit free)](https://www.coursera.org/specializations/machine-learning-introduction)**
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) — the clearest explanations of ML/stats concepts anywhere.
- [Kaggle Learn — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)

### Phase 3 — Deep learning
- **[3Blue1Brown — Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)**
- [fast.ai — Practical Deep Learning for Coders](https://course.fast.ai/)

### Phase 4 — Applied AI / LLMs (the destination)
- [DeepLearning.AI — short courses](https://www.deeplearning.ai/short-courses/) (RAG, agents, LangChain — free)
- [Hugging Face — LLM Course](https://huggingface.co/learn/llm-course)
- [LangChain docs](https://python.langchain.com/) · [LangGraph docs](https://langchain-ai.github.io/langgraph/)
