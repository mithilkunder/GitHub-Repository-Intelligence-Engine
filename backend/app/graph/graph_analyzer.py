import networkx as nx
from app.graph.graph_models import DependencyGraph


class GraphAnalyzer:
    """
    Performs graph analysis on the repository dependency graph.
    """

    def __init__(
        self,
        graph: DependencyGraph,
    ):
        self.graph = graph.graph

    def pagerank(self):
        """
        Returns PageRank score for every file.
        """
        return nx.pagerank(self.graph)

    def cycles(self):
        """
        Returns strongly connected components instead of
        every possible simple cycle.
        """

        components = []

        for component in nx.strongly_connected_components(self.graph):
            if len(component) > 1:
                components.append(sorted(component))

        return components

    def connected_components(self):
        """
        Returns weakly connected components.
        """
        return list(nx.weakly_connected_components(self.graph))

    def shortest_path(
        self,
        source: str,
        target: str,
    ):
        try:
            return nx.shortest_path(
                self.graph,
                source,
                target,
            )

        except nx.NetworkXNoPath:
            return None

        except nx.NodeNotFound:
            return None
