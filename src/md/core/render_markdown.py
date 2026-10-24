from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown

from md.core.exceptions import (
    CannotDecodeError,
    NotAFileError,
    NotAMarkdownError,
)


def render_markdown(file: Path) -> None:
    """Display rendered markdown in terminal"""

    if not (file.exists() and file.is_file()):
        raise NotAFileError(file)

    if file.suffix.lower() != ".md":
        raise NotAMarkdownError(file)

    try:
        contents = file.read_text(encoding="utf-8")
    except UnicodeError as e:
        raise CannotDecodeError(file) from e

    console = Console()
    markdown = Markdown(contents)
    console.print(markdown)
