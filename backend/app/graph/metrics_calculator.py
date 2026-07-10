from app.graph.graph_analyzer import GraphAnalyzer
from app.graph.graph_models import DependencyGraph
from app.graph.repository_metrics import RepositoryMetrics


class MetricsCalculator:
    def calculate(
        self,
        graph: DependencyGraph,
    ) -> RepositoryMetrics:
        analyzer = GraphAnalyzer(graph)

        return RepositoryMetrics(
            total_files=len(graph.nodes),
            dependency_edges=len(graph.edges),
            connected_components=len(analyzer.connected_components()),
            cycles=len(analyzer.cycles()),
            average_dependencies=(len(graph.edges) / max(1, len(graph.nodes))),
        )
