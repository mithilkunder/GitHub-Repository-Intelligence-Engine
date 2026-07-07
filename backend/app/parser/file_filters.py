from pathlib import Path


class FileFilter:
    """
    Utility class responsible for deciding whether a file or directory
    should be ignored during repository scanning.
    """

    IGNORED_DIRECTORIES = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "node_modules",
        "venv",
        ".venv",
        "dist",
        "build",
        ".idea",
        ".vscode",
    }

    IGNORED_FILE_EXTENSIONS = {
        ".pyc",
        ".pyo",
        ".so",
        ".dll",
        ".exe",
        ".class",
    }

    @classmethod
    def should_ignore_directory(cls, directory: Path) -> bool:
        """Return True if the directory should be skipped."""
        return directory.name in cls.IGNORED_DIRECTORIES

    @classmethod
    def should_ignore_file(cls, file: Path) -> bool:
        """Return True if the file should be skipped."""
        return file.suffix in cls.IGNORED_FILE_EXTENSIONS
