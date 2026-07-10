from pathlib import Path

import tree_sitter_python as tspython
from app.visitors.python_visitor import PythonVisitor
from tree_sitter import Language, Parser


class PythonParser:
    def __init__(self):
        self.parser = Parser()

        language = Language(tspython.language())

        self.parser.language = language

    def analyze(self, file: Path):
        code = file.read_bytes()

        tree = self.parser.parse(code)

        visitor = PythonVisitor()

        visitor.visit(tree.root_node)

        return visitor
