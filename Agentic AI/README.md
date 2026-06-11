# Agentic AI Examples

Small LangChain experiments focused on tool usage, agents, and runnable composition.

## Files

- `Agents.py`: city assistant agent with weather and news tools, plus human approval before tool execution
- `toolcalling.py`: basic tool-calling example with a text-length tool
- `owntool.py`: minimal custom tool example using `@tool`
- `sequencerunnable.py`: sequential runnable chain example
- `parallelrunnable.py`: parallel runnable example with short and detailed outputs
- `runnablepassthrough.py`: runnable passthrough example that generates code and explains it
- `newssummarizer.py`: Tavily search plus LLM summarization example

## Requirements

- Python 3.12
- API keys for the scripts you want to run

Example `.env`:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

## Setup

```powershell
cd "Agentic AI"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run Examples

```powershell
python owntool.py
python toolcalling.py
python newssummarizer.py
python Agents.py
```

## Notes

- `Agents.py` uses OpenWeather and Tavily for live tool results.
- Keep `.env` local; it should not be pushed to GitHub.
- These scripts are independent learning examples, not one packaged application.
