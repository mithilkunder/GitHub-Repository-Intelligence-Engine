from pathlib import Path

from app.models.repository_index import RepositoryIndex
from app.models.symbols.import_node import ImportNode
from app.resolver.module_mapper import ModuleMapper


class ImportResolver:
    def __init__(self, index: RepositoryIndex):
        self.mapper = ModuleMapper(index)

    def resolve(
        self,
        source: Path,
        imp: ImportNode,
    ):
        module = imp.module

        if not module:
            return None

        if module.startswith("."):
            target = self.mapper.find_relative(
                source,
                module,
            )

        else:
            target = self.mapper.find_absolute(module)

        return target
