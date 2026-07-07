from pathlib import Path

from app.parser.metadata_extractor import MetadataExtractor
from app.parser.scanner import RepositoryScanner

repo = Path("../data/repositories/requests")

scanner = RepositoryScanner()
files = scanner.scan(repo)

extractor = MetadataExtractor()

metadata = extractor.extract(repo, files)

print(metadata)
