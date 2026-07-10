from dataclasses import dataclass, field


@dataclass
class ImportNode:
    """
    Represents one import statement.
    """

    module: str

    symbols: list[str] = field(default_factory=list)

    alias: str | None = None

    is_relative: bool = False
