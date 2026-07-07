from pathlib import Path

from app.parser.file_filters import FileFilter


class RepositoryScanner:
    """
    Scans a cloned repository and returns a list of source files.
    """

    def scan(self, repository_path: Path) -> list[Path]:
        """
        Recursively scan a repository.

        Parameters
        ----------
        repository_path : Path
            Root directory of the cloned repository.

        Returns
        -------
        list[Path]
            List of valid repository files.
        """

        files: list[Path] = []

        for path in repository_path.rglob("*"):
            if path.is_dir():
                if FileFilter.should_ignore_directory(path):
                    continue

            if path.is_file():
                if FileFilter.should_ignore_file(path):
                    continue

                files.append(path)

        return sorted(files)
