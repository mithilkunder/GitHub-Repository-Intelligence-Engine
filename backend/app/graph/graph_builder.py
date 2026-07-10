from app.graph.graph_models import DependencyGraph
from app.models.repository_index import RepositoryIndex
from app.resolver.import_resolver import ImportResolver


class GraphBuilder:
    """
    Builds a file-to-file dependency graph.
    """

    def build(
        self,
        index: RepositoryIndex,
    ) -> DependencyGraph:
        graph = DependencyGraph()

        resolver = ImportResolver(index)

        for file in index.files:
            graph.add_node(file.relative_path)

            if file.language != "Python":
                continue

            for imp in file.imports:
                target = resolver.resolve(
                    file.path,
                    imp,
                )

                if target is None:
                    continue

                graph.add_node(str(target.relative_to(index.root_path)))

                graph.add_edge(
                    file.relative_path,
                    str(target.relative_to(index.root_path)),
                )

        return graph
