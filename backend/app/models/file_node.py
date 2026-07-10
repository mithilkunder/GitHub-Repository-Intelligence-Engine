from dataclasses import dataclass, field
from pathlib import Path

from app.models.symbols.class_node import ClassNode
from app.models.symbols.function_node import FunctionNode
from app.models.symbols.import_node import ImportNode


@dataclass
class FileNode:
    """
    Represents one source file inside a repository.
    """

    path: Path

    relative_path: str

    language: str

    extension: str

    size: int

    encoding: str = "utf-8"

    sha256: str | None = None

    imports: list[ImportNode] = field(default_factory=list)

    classes: list[ClassNode] = field(default_factory=list)

    functions: list[FunctionNode] = field(default_factory=list)

    chunks: list[str] = field(default_factory=list)

    embedding_ids: list[str] = field(default_factory=list)

    summary: str | None = None
