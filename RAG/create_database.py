from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

base_dir = Path(__file__).resolve().parent
pdf_path = base_dir / "document loaders" / "book.pdf"

data = PyPDFLoader(str(pdf_path))
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

embedding_model = MistralAIEmbeddings()

persist_dir = base_dir / "chroma_db"

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=str(persist_dir)
)