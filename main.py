from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_store import retriever as retrieve

# load model 
model = OllamaLLM(model="llama3.2:1b")

template = """
You are expert in answering quiestions about a restaurant

Here are some relevent reviews : {reviews}

Here is a question to answer : {question}
"""
# prompt template 
prompt = ChatPromptTemplate.from_template(template)

while 1:

    user_prompt = input("Hello there i am Agent Cudos what can help you today ( q to quit ) : ")

    if user_prompt == "q":
        print("Bye")        
        break
    else:
        # chain pipeline *LCEL 
        chain = prompt | model
        reviews = retrieve.invoke(user_prompt)
        response = chain.invoke({"reviews" : reviews, "question" : user_prompt})
        print(response)
