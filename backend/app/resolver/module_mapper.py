from pathlib import Path

from app.models.repository_index import RepositoryIndex


class ModuleMapper:
    """
    Maps Python module names to repository files.
    """

    def __init__(self, index: RepositoryIndex):
        self.index = index
        self.module_map = {}

        for file in index.files:
            if file.extension != ".py":
                continue

            rel = Path(file.relative_path)

            parts = list(rel.parts)

            if parts[-1] == "__init__.py":
                parts = parts[:-1]
            else:
                parts[-1] = rel.stem

            module = ".".join(parts)

            self.module_map[module] = file.path

    def find_absolute(self, module: str):
        return self.module_map.get(module)

    def find_relative(
        self,
        source: Path,
        module: str,
    ):
        level = len(module) - len(module.lstrip("."))

        module = module.lstrip(".")

        current = source.parent

        for _ in range(max(0, level - 1)):
            current = current.parent

        if module:
            target = current.joinpath(*module.split("."))

        else:
            target = current

        py = target.with_suffix(".py")

        if py.exists():
            return py

        init = target / "__init__.py"

        if init.exists():
            return init

        return None
