from dataclasses import dataclass, field


@dataclass
class ClassNode:
    """
    Represents a Python class.
    """

    name: str

    line: int

    base_classes: list[str] = field(default_factory=list)

    methods: list[str] = field(default_factory=list)

    docstring: str | None = None
