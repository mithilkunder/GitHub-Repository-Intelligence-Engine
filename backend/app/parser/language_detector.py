from pathlib import Path


class LanguageDetector:
    """
    Detect programming languages based on file names and extensions.
    """

    EXTENSION_MAP = {
        ".py": "Python",
        ".ipynb": "Jupyter Notebook",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".jsx": "React JSX",
        ".tsx": "React TSX",
        ".java": "Java",
        ".cpp": "C++",
        ".cc": "C++",
        ".c": "C",
        ".h": "C/C++ Header",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".php": "PHP",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".kt": "Kotlin",
        ".scala": "Scala",
        ".r": "R",
        ".m": "MATLAB",
        ".sql": "SQL",
        ".html": "HTML",
        ".css": "CSS",
        ".scss": "SCSS",
        ".json": "JSON",
        ".xml": "XML",
        ".yaml": "YAML",
        ".yml": "YAML",
        ".toml": "TOML",
        ".ini": "INI",
        ".cfg": "Config",
        ".md": "Markdown",
        ".txt": "Text",
        ".sh": "Shell",
        ".bat": "Batch",
    }

    SPECIAL_FILENAMES = {
        "Dockerfile": "Docker",
        "Makefile": "Makefile",
        "README": "Markdown",
        "README.md": "Markdown",
        "LICENSE": "License",
        ".gitignore": "Git Ignore",
        ".dockerignore": "Docker Ignore",
        ".coveragerc": "Coverage Config",
        ".editorconfig": "Editor Config",
        ".git-blame-ignore-revs": "Git Config",
        "CODEOWNERS": "GitHub",
    }

    def detect(self, file: Path) -> str:
        """
        Detect the language/type of a file.
        """

        if file.name in self.SPECIAL_FILENAMES:
            return self.SPECIAL_FILENAMES[file.name]

        return self.EXTENSION_MAP.get(file.suffix.lower(), "Unknown")
