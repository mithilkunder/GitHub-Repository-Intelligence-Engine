from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"

REPOSITORIES_DIR = DATA_DIR / "repositories"

VECTOR_DB_DIR = DATA_DIR / "vector_db"

CACHE_DIR = DATA_DIR / "cache"

UPLOADS_DIR = DATA_DIR / "uploads"

for directory in [
    DATA_DIR,
    REPOSITORIES_DIR,
    VECTOR_DB_DIR,
    CACHE_DIR,
    UPLOADS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

APP_NAME = "RepoMind"

VERSION = "0.1.0"