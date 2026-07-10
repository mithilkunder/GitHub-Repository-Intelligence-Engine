from dataclasses import dataclass, field

import networkx as nx


@dataclass
class DependencyGraph:
    """
    Represents the repository dependency graph.
    """

    graph: nx.DiGraph = field(default_factory=nx.DiGraph)

    @property
    def nodes(self):
        return list(self.graph.nodes)

    @property
    def edges(self):
        return list(self.graph.edges)

    def add_node(self, node: str):
        self.graph.add_node(node)

    def add_edge(self, source: str, target: str):
        self.graph.add_edge(source, target)
