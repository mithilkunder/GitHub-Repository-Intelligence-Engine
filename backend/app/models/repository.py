from dataclasses import dataclass


@dataclass
class RepositoryMetadata:
    """
    Internal representation of repository metadata.
    """

    name: str
    total_files: int
    main_language: str

    has_readme: bool
    has_license: bool

    has_git: bool

    has_docs: bool

    has_tests: bool

    has_docker: bool

    has_docker_compose: bool

    has_github_actions: bool

    has_kubernetes: bool

    package_manager: str

    project_type: str
