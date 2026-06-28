from app.schemas.repository import RepositoryCloneRequest

request = RepositoryCloneRequest(url="https://github.com/psf/requests")

print(request)
