from collections import Counter
from pathlib import Path

from app.parser.language_detector import LanguageDetector
from app.parser.scanner import RepositoryScanner

scanner = RepositoryScanner()
detector = LanguageDetector()

repository = Path("../data/repositories/requests")

files = scanner.scan(repository)

counter = Counter()

for file in files:
    language = detector.detect(file)
    counter[language] += 1

print("\nLanguage Statistics\n")

for language, count in counter.most_common():
    print(f"{language:20} {count}")
