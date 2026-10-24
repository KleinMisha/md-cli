from pathlib import Path
from typing import Annotated

from typer import Argument, Exit, Typer, echo

from md.core.exceptions import MarkdownError
from md.core.render_markdown import render_markdown

app = Typer(no_args_is_help=True)


@app.command()
def render(file: Annotated[Path, Argument(help="Path to markdown file.")]) -> None:
    """Render a markdown file."""
    try:
        render_markdown(file)
        raise Exit(code=0)
    except MarkdownError as e:
        echo(f"{type(e).__name__} : {e!s}")
        raise Exit(code=1)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
