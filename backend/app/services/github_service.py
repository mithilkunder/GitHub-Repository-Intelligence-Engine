from pathlib import Path
from urllib.parse import urlparse

from app.core.config import REPOSITORIES_DIR
from git import GitCommandError, Repo


class GitHubService:
    """
    Service responsible for interacting with GitHub repositories.
    """

    def parse_repository_url(self, url: str) -> tuple[str, str]:
        """
        Extract owner and repository name from a GitHub URL.

        Example:
        https://github.com/psf/requests
        -> ("psf", "requests")
        """

        parsed = urlparse(url)

        if parsed.netloc != "github.com":
            raise ValueError("Only github.com URLs are supported.")

        path_parts = parsed.path.strip("/").split("/")

        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub repository URL.")

        owner = path_parts[0]
        repository = path_parts[1].replace(".git", "")

        return owner, repository

    def get_local_repository_path(self, repository_name: str) -> Path:
        """
        Return the local path where the repository will be cloned.
        """

        return REPOSITORIES_DIR / repository_name

    def clone_repository(self, url: str) -> dict:
        """
        Clone a GitHub repository and return metadata.
        """

        owner, repository_name = self.parse_repository_url(url)

        local_path = self.get_local_repository_path(repository_name)

        if local_path.exists():
            raise FileExistsError(f"Repository '{repository_name}' already exists.")

        try:
            repo = Repo.clone_from(url, local_path)

            return {
                "success": True,
                "repository_name": repository_name,
                "owner": owner,
                "default_branch": repo.active_branch.name,
                "local_path": str(local_path),
            }

        except GitCommandError as error:
            raise RuntimeError(f"Failed to clone repository: {error}") from error
