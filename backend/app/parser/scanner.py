import os
from pathlib import Path

from app.parser.file_filters import FileFilter


class RepositoryScanner:
    """
    Scans a repository while skipping ignored directories.
    """

    def scan(self, repository_path: Path) -> list[Path]:
        files: list[Path] = []

        for root, dirnames, filenames in os.walk(repository_path):
            # Prevent os.walk from entering ignored directories
            dirnames[:] = [
                d for d in dirnames if not FileFilter.should_ignore_directory(Path(d))
            ]

            root_path = Path(root)

            for filename in filenames:
                file = root_path / filename

                if FileFilter.should_ignore_file(file):
                    continue

                files.append(file)

        return sorted(files)
