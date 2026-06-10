from langchain_community.document_loaders import WebBaseLoader

url = "https://www.airtelxstream.in/"

data = WebBaseLoader(url).load()

print(data[0].page_content)