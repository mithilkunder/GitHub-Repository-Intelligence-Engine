from app.models.symbols.class_node import ClassNode
from app.models.symbols.function_node import FunctionNode
from app.models.symbols.import_node import ImportNode
from tree_sitter import Node


class PythonVisitor:
    """
    Extract structured information from a Python AST.
    """

    def __init__(self):
        self.imports: list[ImportNode] = []
        self.classes: list[ClassNode] = []
        self.functions: list[FunctionNode] = []

    def visit(self, node: Node):
        self._walk(node)

    def _walk(self, node: Node):
        # ----------------------------
        # import os
        # import numpy as np
        # ----------------------------

        if node.type == "import_statement":
            text = node.text.decode("utf-8")

            module = text.replace("import", "").strip()

            self.imports.append(
                ImportNode(
                    module=module,
                    is_relative=False,
                )
            )

        # ----------------------------
        # from x import y
        # ----------------------------

        elif node.type == "import_from_statement":
            text = node.text.decode("utf-8")

            try:
                before, after = text.split("import", 1)

                module = before.replace("from", "").strip()

                symbols = [x.strip() for x in after.split(",")]

            except Exception:
                module = text

                symbols = []

            self.imports.append(
                ImportNode(
                    module=module,
                    symbols=symbols,
                    is_relative=module.startswith("."),
                )
            )

        # ----------------------------
        # class
        # ----------------------------

        elif node.type == "class_definition":
            name = node.child_by_field_name("name")

            if name:
                self.classes.append(
                    ClassNode(
                        name=name.text.decode("utf-8"),
                        line=node.start_point[0] + 1,
                    )
                )

        # ----------------------------
        # function
        # ----------------------------

        elif node.type == "function_definition":
            name = node.child_by_field_name("name")

            if name:
                self.functions.append(
                    FunctionNode(
                        name=name.text.decode("utf-8"),
                        line=node.start_point[0] + 1,
                    )
                )

        # ----------------------------

        for child in node.children:
            self._walk(child)
