from pyvis.network import Network
from langchain_community.graph_vectorstores.networkx import documents_to_networkx
def visualize(docs, file_name="graph"):
        net = Network(
            notebook=False,
            cdn_resources="in_line",
            bgcolor="#222222",
            font_color="white",
            height="750px",
            width="100%",
        )
        G = documents_to_networkx(docs, tag_nodes=False)

        net.from_nx(G)
        html = net.generate_html(notebook=False)
        with open("092025_RAG-Challenge/"+file_name + ".html", "w", encoding="utf-8") as f:
            f.write(html)