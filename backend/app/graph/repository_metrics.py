from dataclasses import dataclass


@dataclass
class RepositoryMetrics:
    total_files: int

    dependency_edges: int

    connected_components: int

    cycles: int

    average_dependencies: float
