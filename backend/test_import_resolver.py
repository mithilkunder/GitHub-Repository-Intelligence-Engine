from pathlib import Path

from app.indexer.repository_indexer import RepositoryIndexer
from app.resolver.import_resolver import ImportResolver

repo = Path("../data/repositories/requests")

index = RepositoryIndexer().build(repo)

resolver = ImportResolver(index)

count = 0

for file in index.files:
    if file.language != "Python":
        continue

    for imp in file.imports:
        resolved = resolver.resolve(
            file.path,
            imp,
        )

        if resolved:
            print("=" * 70)
            print("Source :", file.relative_path)
            print("Import :", imp.module)
            print("Target :", resolved)
            print()

            count += 1

            if count == 15:
                raise SystemExit
