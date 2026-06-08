# Learning GenAI

Small hands-on LangChain examples for chat models and embedding models.

## What is in this repo

- `chatmodels/chat.py`  
  Gemini chat example using `init_chat_model`.

- `chatmodels/chatbot.py`  
  Terminal chatbot backed by Mistral.

- `chatmodels/UIchatbot.py`  
  Streamlit mood-based chatbot UI backed by Mistral.

- `chatmodels/huggingface.py`  
  Hugging Face endpoint chat example.

- `chatmodels/localmodel.py`  
  Local Hugging Face pipeline chat example.

- `embeddingmodels/embedding.py`  
  Gemini embedding example.

- `embeddingmodels/huggingface_embedding.py`  
  Hugging Face embedding example.

## Requirements

- Python 3.12
- A virtual environment
- API keys in `.env` for the providers you want to use

Example `.env` entries:

```env
GOOGLE_API_KEY=your_google_key
MISTRAL_API_KEY=your_mistral_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run examples

Gemini chat:

```powershell
python chatmodels\chat.py
```

Terminal chatbot:

```powershell
python chatmodels\chatbot.py
```

Streamlit UI chatbot:

```powershell
streamlit run chatmodels\UIchatbot.py
```

Gemini embeddings:

```powershell
python embeddingmodels\embedding.py
```

Hugging Face embeddings:

```powershell
python embeddingmodels\huggingface_embedding.py
```

## Notes

- `.env` is intentionally ignored and should never be committed.
- `chatmodels/localmodel.py` may require additional local ML runtime dependencies depending on your system.
- This repo is for learning and experimentation, so each script is kept simple and independent.
