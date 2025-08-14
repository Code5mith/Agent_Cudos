import pandas as pd
import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# semantic embadding
embaddings = OllamaEmbeddings(model="mxbai-embed-large:latest")

db_path = "./review_db"

df = pd.read_csv("Restaurant_Reviews.tsv", sep="\t")

if not os.path.exists(db_path):
    documents = []
    ids = []

    for i, row in df.iterrows():
        # standardized format required by LangChain's vector stores
        document = Document(
            page_content=row["Review"] + " " + str(row["Liked"]),
            metadata={"id" : str(i)},
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))
    
    vectorstore = Chroma(
        collection_name="restaurant_reviews",
        persist_directory = db_path,
        embedding_function = embaddings
    )

    vectorstore.add_documents(documents=documents, ids=ids)


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5} # review count
)
