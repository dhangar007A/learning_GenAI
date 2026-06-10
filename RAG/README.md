# RAG Book Assistant

A small Retrieval-Augmented Generation project built with LangChain, Chroma, Streamlit, and Mistral AI.

The project lets you:

- load a PDF
- split it into chunks
- create embeddings with `MistralAIEmbeddings`
- store the vectors in Chroma
- ask grounded questions against the indexed document

## Tech Stack

- `Streamlit` for the UI
- `LangChain` for orchestration
- `Mistral AI` for chat and embeddings
- `Chroma` for local vector storage
- `PyPDFLoader` for PDF ingestion

## Project Files

- `app.py`: Streamlit UI for upload, indexing, and Q&A
- `create_database.py`: script to build a local Chroma database from the sample PDF
- `main.py`: CLI-based question answering interface
- `requirements.txt`: Python dependencies

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file inside `RAG/`.

Required environment variable:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

## Run The Streamlit App

From the `RAG/` directory:

```bash
streamlit run app.py
```

## Run The CLI Version

From the `RAG/` directory:

```bash
python main.py
```

## Create The Vector Database

If you want to build the database from the sample PDF directly:

```bash
python create_database.py
```

The Streamlit app can also create the vector database from an uploaded PDF.

## Notes

- This project is configured for `Mistral AI` only.
- OpenAI dependencies and embeddings are not used in the current setup.
- Generated local vector data is ignored through `.gitignore`.
- The local `.env` file is ignored and should not be committed.
