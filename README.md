# AI Engineering Journey

My self-paced path from full-stack development into **applied AI / AI-engineering** — LLMs, RAG, agents, LangChain/LangGraph. This repo is a public learning log: every assignment, with code and notes, organized by phase and week. Mentored daily, reviewed like code.

> **🎓 Roadmap complete (Phases 1–4).** From vectorized NumPy → pandas/EDA → embeddings & cosine similarity → RAG from scratch → tool calling → agents → LangGraph → LLM-as-judge evals → a deployable tool-using agent → advanced agent patterns (memory, human-in-the-loop, multi-agent supervisor, reflection). Built every layer by hand before reaching for frameworks.

> Starting point: ~1 year full-stack (React/Next.js + Python/Django/Celery/Redis/Elasticsearch). Goal: ship real applied-AI systems.

## Roadmap

> **Track: lean foundation → applied AI.** Goal is *AI-engineering* (building on LLMs), not ML research — so I keep the math/ML foundation thin and jump fast to building.

| Phase | Focus |
|-------|-------|
| 1 | Python for data (NumPy/Pandas) + math *intuition* ✅ |
| 2 | **Applied AI / LLMs** (prompting, RAG, vector DBs, tool calling, LangChain, LangGraph, agents, evals) ← focus |
| 3 | Build & ship 2–3 deployed portfolio projects |
| 4 | Specialize |
| _opt_ | _Deferred deep-dives: classic ML (scikit-learn), deep-learning internals (PyTorch) — revisit only if a real need appears_ |

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

phase-2-applied-ai-llms/
    p2-a1-first-llm-calls/     # first Claude API calls + prompting basics
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

| 2026-06-29 | Phase 2 · P2-A1 First LLM calls + prompting | ✅ done | 8.5/10 |
| 2026-06-29 | Phase 2 · P2-A2 Structured output (LLM → JSON → DataFrame) | ✅ done | 9.5/10 |
| 2026-06-29 | Phase 2 · P2-A3 Embeddings & semantic search | ✅ done | 9.5/10 |
| 2026-06-29 | Phase 2 · P2-A4 RAG end-to-end (retrieve + generate) | ✅ done | 10/10 |
| 2026-06-29 | Phase 2 · P2-A5 Tool calling (the foundation of agents) | ✅ done | 10/10 |
| 2026-06-29 | Phase 2 · P2-A6 Build an agent (the multi-step loop) | ✅ done | 10/10 |
| 2026-06-29 | Phase 2 · P2-A7 The same agent, in LangGraph | ✅ done | 9.5/10 |
| 2026-06-29 | Phase 2 · P2-A8 Evaluate your RAG system (capstone) | ✅ done | 10/10 |

> 🏁 **Phase 2 complete** — prompting, structured output, embeddings, RAG, tool calling, agents (from scratch + LangGraph), and an LLM-as-judge eval harness. Next: **Phase 3 — ship a deployed project.**

| 2026-06-30 | Phase 3 · Research Assistant Agent · M1 Agent core | ✅ done | — |
| 2026-06-30 | Phase 3 · Research Assistant Agent · M3 Agent evals | ✅ done | — |

> 🏁 **Phase 3 — Research Assistant Agent shipped** (agent core + eval harness). UI/deploy intentionally skipped (deploy process documented in the project README).

| 2026-06-30 | Phase 4 · Advanced Agents · P4-A1 Persistent memory | ✅ done | 10/10 |
| 2026-06-30 | Phase 4 · Advanced Agents · P4-A2 Human-in-the-loop | ✅ done | 10/10 |
| 2026-06-30 | Phase 4 · Advanced Agents · P4-A3 Multi-agent (supervisor) | ✅ done | 10/10 |
| 2026-06-30 | Phase 4 · Advanced Agents · P4-A4 Reflection (self-correction) | ✅ done | 10/10 |

> 🏁 **Phase 4 complete** — persistent memory, human-in-the-loop, multi-agent supervisor, reflection.
> 🎓 **Roadmap complete** — from NumPy basics to production-pattern agent systems, built understanding every layer.

**Phase 4 — Advanced Agents** (specialization): persistent memory → human-in-the-loop → multi-agent (supervisor) → reflection.

**Phase 3 project:** [`phase-3-projects/research-agent/`](phase-3-projects/research-agent/) — a deployed tool-using agent (LangGraph + Wikipedia/calculator tools + Streamlit UI + eval harness).

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

### Phase 1 — Python for data + math intuition ✅
- **[Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas)** — short, hands-on, mirrors what you're doing.
- [Corey Schafer — Pandas tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — the canonical pandas walkthrough on YouTube.
- [pandas docs — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [NumPy — broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- **[3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)** — intuition only, no grinding proofs.

### Phase 2 — Applied AI / LLMs (now — the destination)
- **[OpenAI — API docs](https://platform.openai.com/docs/guides/text)** — the SDK we build on (using OpenAI for now).
- **[OpenAI — Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)** · [Anthropic's prompt guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) (concepts transfer to either).
- [DeepLearning.AI — short courses](https://www.deeplearning.ai/short-courses/) (RAG, agents, LangChain — free, ~1 hr each).
- [Hugging Face — LLM Course](https://huggingface.co/learn/llm-course)
- [LangChain docs](https://python.langchain.com/) · [LangGraph docs](https://langchain-ai.github.io/langgraph/)

### Optional deep-dives (deferred — only if a real need appears)
- [Andrew Ng — ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction) · [StatQuest](https://www.youtube.com/@statquest) — classic ML.
- [3Blue1Brown — Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) · [fast.ai](https://course.fast.ai/) — deep-learning internals.
