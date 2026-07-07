import hashlib
from pathlib import Path

from app.models.file_node import FileNode
from app.models.repository_index import RepositoryIndex
from app.parser.language_detector import LanguageDetector
from app.parser.metadata_extractor import MetadataExtractor
from app.parser.scanner import RepositoryScanner


class RepositoryIndexer:
    """
    Builds a RepositoryIndex from a cloned repository.
    """

    def __init__(self):
        self.scanner = RepositoryScanner()
        self.detector = LanguageDetector()
        self.extractor = MetadataExtractor()

    def build(self, repository_path: Path) -> RepositoryIndex:
        files = self.scanner.scan(repository_path)

        metadata = self.extractor.extract(
            repository_path,
            files,
        )

        nodes = []

        for file in files:
            node = FileNode(
                path=file,
                relative_path=str(file.relative_to(repository_path)),
                language=self.detector.detect(file),
                extension=file.suffix,
                size=file.stat().st_size,
                sha256=self.calculate_hash(file),
            )

            nodes.append(node)

        return RepositoryIndex(
            repository_name=repository_path.name,
            root_path=str(repository_path),
            metadata=metadata,
            files=nodes,
        )

    @staticmethod
    def calculate_hash(file: Path) -> str:
        return hashlib.sha256(file.read_bytes()).hexdigest()
