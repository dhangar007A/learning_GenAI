from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello this is Abhishek",
    "Hello im here to help you",
    "And you are my friend"
]

vector = embedding.embed_documents(texts)

print(vector)