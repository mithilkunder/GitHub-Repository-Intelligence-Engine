from app.services.github_service import GitHubService


class RepositoryService:
    """
    High-level service responsible for repository operations.
    """

    def __init__(self) -> None:
        self.github_service = GitHubService()

    def clone_repository(self, url: str) -> dict:
        """
        Clone a repository using GitHubService.
        """
        return self.github_service.clone_repository(url)
