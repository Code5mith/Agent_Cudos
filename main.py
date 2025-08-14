from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# from vector import retriever

# load model 
model = OllamaLLM(model="llama3.2:1b")

template = """
You are expert in answering quiestions about a restaurant

Here are some relevent reviews : {reviews}

Here is a question to answer : {question}
"""
# prompt template 
prompt = ChatPromptTemplate.from_template(template)

# chain pipeline *LCEL 
chain = prompt | model

response = chain.invoke({"reviews" : [], "question" : "What is the most popular food"})

print(response)
