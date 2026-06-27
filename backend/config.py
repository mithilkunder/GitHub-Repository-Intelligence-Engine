from pathlib import Path

# Root directory of the backend
BASE_DIR = Path(__file__).resolve().parent

# Folder where cloned repositories will be stored
REPOSITORIES_DIR = BASE_DIR.parent / "repositories"

# Create repositories folder if it doesn't exist
REPOSITORIES_DIR.mkdir(parents=True, exist_ok=True)

APP_NAME = "RepoMind"

VERSION = "0.1.0"