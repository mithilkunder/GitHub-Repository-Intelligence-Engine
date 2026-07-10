from pathlib import Path

from app.parsers.python_parser import PythonParser

parser = PythonParser()

file = Path("../data/repositories/requests/src/requests/api.py")

analysis = parser.analyze(file)

print("\nImports\n")

for imp in analysis.imports:
    print(imp)

print("\nClasses\n")

for cls in analysis.classes:
    print(cls)

print("\nFunctions\n")

for func in analysis.functions:
    print(func)
