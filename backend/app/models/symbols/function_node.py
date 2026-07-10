from dataclasses import dataclass, field


@dataclass
class FunctionNode:
    """
    Represents a Python function.
    """

    name: str

    line: int

    is_async: bool = False

    decorators: list[str] = field(default_factory=list)

    docstring: str | None = None
