from app.api.v1.endpoints.repositories import router as repository_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(repository_router)
