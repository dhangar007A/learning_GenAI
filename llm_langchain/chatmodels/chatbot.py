from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatMistralAI(model = "mistral-small-2506", temperature = 0.9)
message = [
    SystemMessage(content = "You are a funny ai assistant."),
]

print("Ask me anything! (type 'exit' to quit)") 

while True:
    prompt = input("You: ")
    message.append(HumanMessage(content = prompt))
    if prompt.lower() == "exit":
        break
    response = model.invoke(message)
    message.append(AIMessage(content = response.content))
    print("Bot:" ,response.content)