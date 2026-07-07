from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FileNode:
    """
    Represents a single file inside a repository.
    """

    path: Path

    relative_path: str

    language: str

    extension: str

    size: int

    encoding: str = "utf-8"

    sha256: str | None = None

    imports: list[str] = field(default_factory=list)

    functions: list[str] = field(default_factory=list)

    classes: list[str] = field(default_factory=list)

    chunks: list[str] = field(default_factory=list)

    embedding_ids: list[str] = field(default_factory=list)

    summary: str | None = None
