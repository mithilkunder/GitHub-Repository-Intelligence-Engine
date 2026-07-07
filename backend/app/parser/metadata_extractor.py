from collections import Counter
from pathlib import Path

from app.models.repository import RepositoryMetadata
from app.parser.language_detector import LanguageDetector


class MetadataExtractor:
    """
    Extract repository level metadata.
    """

    def __init__(self):
        self.detector = LanguageDetector()

    def extract(
        self,
        repository_path: Path,
        files: list[Path],
    ) -> RepositoryMetadata:
        language_counter = Counter()

        for file in files:
            language = self.detector.detect(file)
            language_counter[language] += 1

        names = {file.name for file in files}

        directories = {path.parent.name for path in files}

        return RepositoryMetadata(
            name=repository_path.name,
            total_files=len(files),
            main_language=language_counter.most_common(1)[0][0],
            has_readme=self.has_readme(names),
            has_license=self.has_license(names),
            has_git=(repository_path / ".git").exists(),
            has_docs=self.has_docs(directories),
            has_tests=self.has_tests(directories),
            has_docker=self.has_docker(names),
            has_docker_compose=self.has_docker_compose(names),
            has_github_actions=self.has_github_actions(repository_path),
            has_kubernetes=self.has_kubernetes(repository_path),
            package_manager=self.detect_package_manager(names),
            project_type=self.detect_project_type(names),
        )

    @staticmethod
    def has_readme(names: set[str]) -> bool:
        return any(name.startswith("README") for name in names)

    @staticmethod
    def has_license(names: set[str]) -> bool:
        return any(name.startswith("LICENSE") for name in names)

    @staticmethod
    def has_docs(directories: set[str]) -> bool:
        return "docs" in directories

    @staticmethod
    def has_tests(directories: set[str]) -> bool:
        return "tests" in directories or "test" in directories

    @staticmethod
    def has_docker(names: set[str]) -> bool:
        return "Dockerfile" in names

    @staticmethod
    def has_docker_compose(names: set[str]) -> bool:
        return any(
            name in names
            for name in (
                "docker-compose.yml",
                "docker-compose.yaml",
                "compose.yaml",
            )
        )

    @staticmethod
    def has_github_actions(repository_path: Path) -> bool:
        return (repository_path / ".github" / "workflows").exists()

    @staticmethod
    def has_kubernetes(repository_path: Path) -> bool:
        return (repository_path / "k8s").exists() or (repository_path / "helm").exists()

    @staticmethod
    def detect_package_manager(names: set[str]) -> str:
        if "uv.lock" in names:
            return "uv"

        if "poetry.lock" in names:
            return "Poetry"

        if "requirements.txt" in names:
            return "pip"

        if "package.json" in names:
            return "npm"

        if "pom.xml" in names:
            return "Maven"

        if "Cargo.toml" in names:
            return "Cargo"

        if "go.mod" in names:
            return "Go Modules"

        return "Unknown"

    @staticmethod
    def detect_project_type(names: set[str]) -> str:
        if "manage.py" in names:
            return "Django"

        if "package.json" in names:
            return "JavaScript / Node.js"

        if "pyproject.toml" in names:
            return "Python"

        if "Cargo.toml" in names:
            return "Rust"

        if "pom.xml" in names:
            return "Java"

        if "go.mod" in names:
            return "Go"

        return "Unknown"
