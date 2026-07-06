from app.services.github_service import GitHubService

service = GitHubService()

result = service.clone_repository("https://github.com/psf/requests")

print(result)
