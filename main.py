from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# import model 
model = OllamaLLM(model="llama3.2")

# chat template 
template = """
You are expert in answering quiestions about a pizza restaurant

Here are some relevent reviews : { review }

Here is a question to answer : { question }

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while 1:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews" : reviews, "question" : question})
    print(result)
        