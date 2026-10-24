from pathlib import Path


class MarkdownError(Exception): ...


class NotAMarkdownError(MarkdownError):
    """Improper file type"""

    def __init__(self, file: Path) -> None:
        super().__init__(f"Not a markdown file: {file}")


class NotAFileError(MarkdownError):
    """is not a file"""

    def __init__(self, file: Path) -> None:
        super().__init__(f"File not found: {file}")


class CannotDecodeError(MarkdownError):
    """Unable to decode the contents using UTF-8"""

    def __init__(self, file: Path) -> None:
        super().__init__(f"Cannot decode {file}")
