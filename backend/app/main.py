from app.api.v1.api import api_router
from app.core.config import APP_NAME, VERSION
from fastapi import FastAPI

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="AI-Powered GitHub Repository Intelligence Engine",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    return {
        "message": "RepoMind Backend Running 🚀",
        "version": VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
