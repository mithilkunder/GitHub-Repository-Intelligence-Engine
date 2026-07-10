from pathlib import Path

from app.graph.graph_analyzer import GraphAnalyzer
from app.graph.graph_builder import GraphBuilder
from app.indexer.repository_indexer import RepositoryIndexer

repo = Path("../data/repositories/requests")

index = RepositoryIndexer().build(repo)

graph = GraphBuilder().build(index)

analyzer = GraphAnalyzer(graph)

print("\nRepository Statistics\n")

print("Nodes:", len(graph.nodes))
print("Edges:", len(graph.edges))

# -----------------------------
# PageRank
# -----------------------------

print("\nTop 10 Most Important Files\n")

ranking = sorted(
    analyzer.pagerank().items(),
    key=lambda x: x[1],
    reverse=True,
)

for node, score in ranking[:10]:
    print(f"{score:.5f}  {node}")

# -----------------------------
# Strongly Connected Components
# -----------------------------

print("\nStrongly Connected Components\n")

cycles = analyzer.cycles()

if not cycles:
    print("None")
else:
    for i, component in enumerate(cycles, start=1):
        print(f"\nComponent {i}")
        for file in component:
            print("  ", file)

# -----------------------------
# Connected Components
# -----------------------------

components = analyzer.connected_components()

print("\nRepository Connectivity\n")

print("Connected Components :", len(components))

largest = max(components, key=len)

print("Largest Component    :", len(largest))

# -----------------------------
# Shortest Path Demo
# -----------------------------

print("\nShortest Path Example\n")

source = "src/requests/api.py"
target = "src/requests/models.py"

path = analyzer.shortest_path(
    source,
    target,
)

if path:
    print(" -> ".join(path))
else:
    print(f"No path found between\n{source}\nand\n{target}")
