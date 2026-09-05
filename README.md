# AI Icebreaker Bot

The LinkedIn Icebreaker Bot is an AI-powered tool that generates personalized conversation starters from LinkedIn profiles. Using Llama 3.2 3B (Ollama) and LlamaIndex, it extracts profile data (via built-in mock data), processes it through a RAG pipeline, and produces tailored insights about a person's career. With the convenient mock data option, you can demonstrate the bot's capabilities without an API key - perfect for testing or presentations. Simply select "Use Mock Data" in the interface to instantly analyze a pre-loaded professional profile.

Available as both a command-line tool and web interface, the bot helps you make meaningful professional connections by replacing generic small talk with relevant, personalized conversation starters based on someone's actual experience and achievements.

---

## About

The AI Icebreaker Bot leverages large language models and retrieval-augmented generation to analyze LinkedIn profiles and generate personalized conversation starters. It's designed to help professionals make meaningful connections by providing relevant, experience-based insights rather than generic small talk.

## Features

- **Vector search** — chunks are embedded and stored in LlamaIndex VectorStoreIndex for search.
- **RAG pipeline** — retrieved chunks are injected into a prompt so the LLM answers strictly from the indexed context (and admits when it doesn't know).
- **Local LLM & embeddings** — powered by [Ollama](https://ollama.com/) (default: `llama3.2` for generation, `nomic-embed-text` for embeddings). No external API calls, no data leaves your machine.
- **Web UI** — a [Gradio](https://www.gradio.app/) chat interface with LinkedIn profile indexing (using mock data by default) with initial facts about the profile and a Chat tab to interact directly with the LLM about the indexed profile.

## Technologies

- **Python 3.13**
- **[LlamaIndex](https://www.llamaindex.ai/)** — orchestration of the RAG chain (`llama-index-core`, `llama-index-embeddings`, `llama-index-llms-ollama`, `llama-index-readers-file`)
- **[Ollama](https://ollama.com/)** — local LLM inference and embeddings
- **[Gradio](https://www.gradio.app/)** — web-based chat UI
- **[uv](https://docs.astral.sh/uv/)** — dependency management and packaging
- **[Pydantic](https://docs.pydantic.dev/)** — configuration/data validation
- **Docker Compose** — runs Ollama and pulls the required models


## Architecture

```
LinkedIn profile ──▶ loader ──▶ text splitter ──▶ embeddings ──▶ LlamaIndex VectorStoreIndex
                                                              │
User question + chat history ──▶ condense (if follow-up) ──▶ retriever ◀───┘
                                                                 │
                                                                 ▼
                                          prompt + context + chat history ──▶ Ollama LLM ──▶ answer
```

Project layout:

```
src/ai_icebreaker_bot/

├── main.py                  # App interaction via the terminal
├── app/app.py               # Gradio app entry point
├── config.py                # Environment-based config
├── loading/                 # LinkedIn profile loading
├── processing/              # Text splitting
├── retrieval/               # Retriever logic
├── llm/                     # Ollama LLM client
└── chains/                  # RAG chain (prompt + retrieval + LLM)
```

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Docker](https://www.docker.com/) and Docker Compose (to run Ollama), **or** a local [Ollama](https://ollama.com/download) installation

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-icebreaker-bot
```

### 2. Start Ollama and pull the required models

```bash
docker compose up -d
```

This starts the Ollama server and automatically pulls `llama3.2:3b` and `nomic-embed-text`.

> Alternatively, if you have Ollama installed locally, run `ollama pull llama3.2:3b` and `ollama pull nomic-embed-text` instead.

### 3. Install dependencies

```bash
uv sync
```

### 4. Run the app

```bash
uv run ai-icebreaker-bot
```

The Gradio UI will be available at `http://127.0.0.1:5000`.
