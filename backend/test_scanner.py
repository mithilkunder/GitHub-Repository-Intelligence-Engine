from pathlib import Path

from app.parser.scanner import RepositoryScanner

scanner = RepositoryScanner()

repository = Path("../data/repositories/requests")

files = scanner.scan(repository)

print(f"\nFound {len(files)} files:\n")

for file in files[:30]:
    print(file)
