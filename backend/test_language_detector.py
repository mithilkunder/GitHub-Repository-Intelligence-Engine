from pathlib import Path

from app.parser.language_detector import LanguageDetector

detector = LanguageDetector()

files = [
    Path("main.py"),
    Path("README.md"),
    Path("Dockerfile"),
    Path("config.yaml"),
    Path("package.json"),
    Path("hello.cpp"),
    Path("unknown.xyz"),
]

for file in files:
    print(f"{file.name:20} -> {detector.detect(file)}")
