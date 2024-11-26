# from urllib.request import Request
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import networkx as nx


app = FastAPI()

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.get('/pipelines/parse')
def parse_pipeline(pipeline: str = Form(...)):
    return {'status': 'parsed'}

# Allow CORS for frontend/backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/pipelines/parse")
async def parse_pipeline(request: Request):
    # Parse the JSON payload
    data = await request.json()
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])

    # Count nodes and edges
    num_nodes = len(nodes)
    num_edges = len(edges)

    # Create a directed graph
    graph = nx.DiGraph()
    graph.add_nodes_from([node['id'] for node in nodes])
    graph.add_edges_from([(edge['source'], edge['target']) for edge in edges])

    # Check if the graph is a DAG
    is_dag = nx.is_directed_acyclic_graph(graph)

    # Return the result
    return {"num_nodes": num_nodes, "num_edges": num_edges, "is_dag": is_dag}
