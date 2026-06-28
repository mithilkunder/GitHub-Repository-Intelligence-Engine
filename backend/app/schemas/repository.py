from pydantic import BaseModel, Field, HttpUrl


class RepositoryCloneRequest(BaseModel):
    """
    Request schema for cloning a GitHub repository.
    """

    url: HttpUrl = Field(
        ...,
        description="Public GitHub repository URL",
        examples=["https://github.com/psf/requests"],
    )


class RepositoryCloneResponse(BaseModel):
    """
    Response schema returned after a successful clone.
    """

    success: bool
    repository_name: str
    owner: str
    default_branch: str
    local_path: str
