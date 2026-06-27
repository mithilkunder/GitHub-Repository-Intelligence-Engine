from fastapi import FastAPI
from config import APP_NAME, VERSION

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="AI Powered GitHub Repository Intelligence Engine"
)


@app.get("/")
def home():
    return {
        "message": "RepoMind Backend Running 🚀",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }