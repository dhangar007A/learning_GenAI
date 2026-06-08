from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

texts = [
    "Hello this is Abhishek",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]

vectors = embeddings.embed_documents(texts)

print(len(vectors))
print(len(vectors[0]))