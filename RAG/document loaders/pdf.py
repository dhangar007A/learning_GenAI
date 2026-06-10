# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import TokenTextSplitter

# data = PyPDFLoader("document loaders/book.pdf").load()

# splitter = TokenTextSplitter(chunk_size=100, chunk_overlap=1)
# chunks = splitter.split_documents(data)

# print(len(chunks))

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)