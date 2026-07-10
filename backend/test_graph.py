from pathlib import Path

from app.graph.graph_builder import GraphBuilder
from app.indexer.repository_indexer import RepositoryIndexer

repo = Path("../data/repositories/requests")

index = RepositoryIndexer().build(repo)

graph = GraphBuilder().build(index)

print("\nNodes :", len(graph.nodes))
print("Edges :", len(graph.edges))

print("\nFirst 20 File Dependencies\n")

for source, target in graph.edges[:20]:
    print(f"{source}  --->  {target}")
