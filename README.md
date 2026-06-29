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
    a1-numpy/                  # vectorized NumPy ops
    a2-pandas-titanic/         # Titanic EDA
    a3-mini-project/           # charts + writeup
  week-02/
    w2-a1-cosine-similarity/   # vectors + cosine similarity (the heart of RAG)
    w2-a2-pandas-for-evals/    # build & score a results table (LLM-eval shape)
```

Each assignment folder holds a notebook (`.ipynb`) or script plus a short `NOTES.md` explaining the approach and what I learned.

## Progress log

| Date | Assignment | Status | Score |
|------|-----------|--------|-------|
| 2026-06-29 | Phase 1 · Week 1 · A1 NumPy (vectorized ops + broadcasting) | ✅ done | 8.5/10 |
| 2026-06-29 | Phase 1 · Week 1 · A2 Pandas EDA (Titanic) | ✅ done | 8/10 |
| 2026-06-29 | Phase 1 · Week 1 · A3 Mini project (charts + writeup) | ✅ done | 8/10 |
| 2026-06-29 | Phase 1 · Week 2 · W2-A1 Cosine similarity (RAG retrieval) | ✅ done | 9.5/10 |
| 2026-06-29 | Phase 1 · Week 2 · W2-A2 Pandas for evals | ✅ done | 9.5/10 |

> 🏁 **Phase 1 complete** — vectorized NumPy, pandas EDA, matplotlib, cosine-similarity/retrieval, and eval scoring. On to **Phase 2: Applied AI / LLMs.**

## What to learn for each task (and where)

Study the "learn" column *before* attempting the task. Each links to the minimum you need — don't over-study, just enough to start.

### Week 1 — done ✅
| Task | Learn this | Where |
|------|-----------|-------|
| A1 — NumPy | arrays, vectorized ops, `axis`, broadcasting | [NumPy: absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) · [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) |
| A2 — Pandas EDA | DataFrame basics, `isnull`/`sum`, `groupby`, `fillna` | [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) · [Corey Schafer pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) |
| A3 — Mini project | matplotlib: `bar`/`hist`, titles & axis labels | [matplotlib — pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) |

### Week 2 — now 🔜
| Task | Learn this | Where |
|------|-----------|-------|
| **W2-A1 — Cosine similarity** | vectors, dot product, vector length (norm), cosine similarity | [3B1B — Essence of Linear Algebra ch.1–4](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · [3B1B — Dot products](https://www.youtube.com/watch?v=LyGKycYT2v0) · [cosine similarity (overview)](https://en.wikipedia.org/wiki/Cosine_similarity) |
| W2-A2 — Pandas for evals | accuracy/precision/recall idea, `groupby` metrics, value_counts | [StatQuest — confusion matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o) · [StatQuest — precision & recall](https://www.youtube.com/watch?v=4jRBRDbJemM) |

> **How to use this:** watch/read the "where" links (aim for ~30–40 min, intuition over completeness), then open the scaffolded notebook and fill in the TODOs. Stuck? That's expected — that's where mentor review comes in.

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
