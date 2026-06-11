# Learning GenAI

Hands-on Python projects for learning GenAI patterns with LangChain, Mistral, Tavily, Chroma, and Streamlit.

## Projects

### `llm_langchain/`
Small examples for chat models and embedding models:

- terminal and Streamlit chatbots
- Gemini and Hugging Face integrations
- local model and embedding experiments

See [llm_langchain/README.md](./llm_langchain/README.md).

### `RAG/`
A Retrieval-Augmented Generation project that indexes PDF content into Chroma and answers grounded questions through a CLI or Streamlit app.

See [RAG/README.md](./RAG/README.md).

### `Agentic AI/`
LangChain agent and runnable examples covering tool calling, parallel runnables, passthrough chains, and a small city assistant agent with weather and news tools.

See [Agentic AI/README.md](./Agentic%20AI/README.md).

## Repository Setup

This repository contains separate learning projects, each with its own `requirements.txt`.

1. Create a virtual environment for the project you want to run.
2. Install that folder's dependencies.
3. Add the required API keys to a local `.env` file.

Example:

```powershell
cd RAG
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables

Different examples use different providers. Depending on what you run, you may need:

```env
MISTRAL_API_KEY=your_mistral_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

## Notes

- Local `.env` files and virtual environments are ignored and should not be committed.
- Some folders are experimental and contain independent scripts rather than one integrated application.
- The repository is intended for learning, so examples stay small and direct.
