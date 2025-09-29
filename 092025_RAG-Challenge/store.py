from graph_rag_example_helpers.datasets.animals import fetch_documents
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_astradb import AstraDBGraphVectorStore
from dotenv import load_dotenv
load_dotenv(override=True)

animals = fetch_documents()
vector_store = AstraDBGraphVectorStore.from_documents(
    collection_name="animals",
    documents=animals,
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
)