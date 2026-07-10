from pathlib import Path

from app.indexer.repository_indexer import RepositoryIndexer

repo = Path("../data/repositories/requests")

index = RepositoryIndexer().build(repo)

print(f"\nRepository: {index.repository_name}")
print(f"Total Files: {index.total_files}")
print(f"Main Language: {index.metadata.main_language}")

print("\nFirst 5 Python Files\n")

count = 0

for file in index.files:
    if file.language != "Python":
        continue

    print("=" * 80)
    print(f"File: {file.relative_path}")
    print(f"Language: {file.language}")
    print(f"Size: {file.size} bytes")

    print("\nImports")
    if file.imports:
        for imp in file.imports:
            print(f"  {imp}")
    else:
        print("  None")

    print("\nClasses")
    if file.classes:
        for cls in file.classes:
            print(f"  {cls}")
    else:
        print("  None")

    print("\nFunctions")
    if file.functions:
        for func in file.functions:
            print(f"  {func}")
    else:
        print("  None")

    print()

    count += 1

    if count == 5:
        break
