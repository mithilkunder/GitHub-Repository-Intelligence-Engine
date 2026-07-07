from pathlib import Path

from app.indexer.repository_indexer import RepositoryIndexer

repo = Path("../data/repositories/requests")

index = RepositoryIndexer().build(repo)

print(f"\nRepository: {index.repository_name}")
print(f"Total Files: {index.total_files}")
print(f"Main Language: {index.metadata.main_language}")

print("\nFirst 10 Files:\n")

for file in index.files[:10]:
    print(f"{file.relative_path:<40}{file.language:<15}{file.size:>8} bytes")
