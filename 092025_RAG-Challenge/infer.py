from langchain_graph_retriever.document_graph import create_graph
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_graph_retriever import GraphRetriever
from langchain_astradb import AstraDBGraphVectorStore
from graph_retriever.strategies import Eager
from visualize import visualize
import networkx as nx
from dotenv import load_dotenv
load_dotenv(override=True)

vector_store = AstraDBGraphVectorStore(
    collection_name="animals2",
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
)
# simple = GraphRetriever(
#     store = vector_store,
#     edges = [("habitat", "habitat"), ("origin", "origin"), ("keywords", "keywords")],
#     strategy = Eager(k=10, start_k=1, max_depth=2),
# )

# simple_results = simple.invoke("Give me all the insects that have 6 legs.")

# for doc in simple_results:
#     print(f"{doc.id}: {doc.page_content}\n {doc.metadata}")

# document_graph = create_graph(
#     documents=simple_results,
#     edges = simple.edges,
# )

document_graph = vector_store.metadata_search(filter={"graph_edges": {"$exists": False}}, n=1000)
visualize(document_graph)