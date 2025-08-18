### **Restaurant Review Q\&A Bot**



https://github.com/user-attachments/assets/4421439e-b3c6-40b9-be31-55f77003187e



This project is a command-line application that acts as a Q\&A bot for a restaurant. It leverages a Retrieval-Augmented Generation (RAG) pipeline built with LangChain to provide insightful, context-aware answers to user questions based on a collection of restaurant reviews.

### **Core Functionality**

The application is designed to answer specific questions by using a two-step process:

1. **Retrieval:** When a user asks a question, the application first queries a vector store to find the most relevant restaurant reviews. This ensures the information is grounded in a specific, provided context.  
2. **Generation:** The relevant reviews, along with the user's original question, are passed to a Large Language Model (LLM). The LLM then generates a concise and accurate answer based *only* on the provided context, preventing factual inaccuracies or "hallucinations."

### **Technologies Used**

* **Python:** The core language for the application.  
* **LangChain:** The framework for building the RAG pipeline.  
* **Ollama:** Used to run the local language model.  
* **llama3.2:** The specific LLM used for text generation.

### **How to Run**

1. Ensure you have Ollama installed and have pulled the llama3.2 model.  
2. Make sure the vector and retriever modules are properly defined and configured to connect to your vector store.  
3. Run the main Python script from your terminal.

```
 python main.py

```
### ** Suggested Prompts **
    - What is the most popular food in the restaurant
    - What is the menu of the restaurant
    - What is the least popular food ...
