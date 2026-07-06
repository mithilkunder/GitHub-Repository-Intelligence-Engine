from app.schemas.repository import (
    RepositoryCloneRequest,
    RepositoryCloneResponse,
)
from app.services.repository_service import RepositoryService
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/repositories", tags=["Repositories"])

repository_service = RepositoryService()


@router.post(
    "/clone",
    response_model=RepositoryCloneResponse,
)
def clone_repository(request: RepositoryCloneRequest):
    """
    Clone a public GitHub repository.
    """
    try:
        result = repository_service.clone_repository(str(request.url))
        return RepositoryCloneResponse(**result)

    except FileExistsError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error),
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )
