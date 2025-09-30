from langchain_graph_retriever.document_graph import create_graph
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_graph_retriever import GraphRetriever
from langchain_astradb import AstraDBVectorStore
from graph_retriever.strategies import Mmr
from visualize import visualize
import networkx as nx
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv(override=True)

edges = [("number_of_legs", "number_of_legs")]

vector_store = AstraDBVectorStore(
    collection_name="animals2",
    embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
)
retriever = GraphRetriever(
    store = vector_store,
    edges = edges,
    strategy = Mmr(k=10, start_k=1, max_depth=2),
)

# docs = vector_store.traversal_search("what animals could be found near a capybara?", k=5, max_depth=2, filter=)

docs = retriever.invoke("What creatures have 8 legs?")

# docs = vector_store.metadata_search(filter={"graph_edges": {"$exists": False}}, n=1000)

# docs = vector_store.metadata_search(n=1000)

for doc in docs:
    print(f"{doc.id}: {doc.page_content}\n {doc.metadata}")
    # print(doc)

document_graph = create_graph(
    documents = docs,
    edges = edges,
)
pos = nx.spring_layout(document_graph)
nx.draw(document_graph, pos, with_labels=True, node_color="lightblue", arrows=True)
plt.show()
# visualize(document_graph)