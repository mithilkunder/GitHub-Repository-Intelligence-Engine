from dataclasses import dataclass, field

from app.models.file_node import FileNode
from app.models.repository import RepositoryMetadata


@dataclass
class RepositoryIndex:
    """
    Central in-memory representation of a repository.
    """

    repository_name: str

    root_path: str

    metadata: RepositoryMetadata

    files: list[FileNode] = field(default_factory=list)

    @property
    def total_files(self) -> int:
        return len(self.files)

    def get_python_files(self) -> list[FileNode]:
        return [file for file in self.files if file.language == "Python"]

    def get_markdown_files(self) -> list[FileNode]:
        return [file for file in self.files if file.language == "Markdown"]
