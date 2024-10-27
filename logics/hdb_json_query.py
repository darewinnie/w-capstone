from langchain_community.document_loaders import CSVLoader
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tqdm import tqdm
import os

load_dotenv()

# Set up embeddings and document loader
embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
loader = CSVLoader("./data/resaleoct23.csv", encoding="windows-1252")
documents = loader.load()

# Specify a directory to persist the database
persist_directory = "./chroma_db"

# Check if Chroma DB already exists
if not os.path.exists(persist_directory):
    print("Creating and persisting Chroma database...")
    # Generate embeddings with a progress bar and collect them in a list
    embedded_documents = []
    for doc in tqdm(documents, desc="Processing documents"):
        embedded_documents.append(doc)

    # Create Chroma database with all embedded documents
    db = Chroma.from_documents(
        embedded_documents, embedding_function, persist_directory=persist_directory
    )
    db.persist()  # Save the database to disk
    print("Chroma database created and persisted.")
else:
    # Load the persisted Chroma database
    print("Loading persisted Chroma database...")
    db = Chroma(
        persist_directory=persist_directory, embedding_function=embedding_function
    )

retriever = db.as_retriever(search_kwargs={"k": 2000})
print("Chroma database is ready for use.")


# Template for the model prompt
template = """You will be provided with customer service queries about hdb town and resale price from jan to october 2024.
Please note month : "2024-10" means October 2024
  Your response must start with Ans:
Please provide answer based on:
{context}


Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Set up the model
llm = ChatOpenAI(
    model="gpt-4o", temperature=0, max_tokens=None, timeout=None, max_retries=2
)


# Define the chain
def query_chain(question):
    print("Retrieving documents...")
    # Retrieve relevant documents
    context_docs = retriever.get_relevant_documents(question)
    context = "\n".join(
        [doc.page_content for doc in context_docs]
    )  # Combine documents as context
    formatted_prompt = prompt.format_prompt(context=context, question=question)
    # Stream the response
    for chunk in llm.stream(formatted_prompt.to_messages()):
        yield chunk


# Updated this part onwards. Use hdb_json_2 in your main.py file
def hdb_json_2(query):
    # Invoke the chain with a sample question
    for chunk in query_chain(query):
        print(chunk.content, end="")


my_query = "What was the average resale price in Oct 2024?"
print(hdb_json_2(my_query))
