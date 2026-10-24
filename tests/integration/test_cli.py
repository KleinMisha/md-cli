from pathlib import Path

from typer.testing import CliRunner

from md.cli.entrypoint import app

runner = CliRunner()


def test_render_markdown_file(tmp_path: Path) -> None:
    """A valid Markdown file renders successfully."""
    markdown_file = tmp_path / "example.md"
    markdown_file.write_text("# Hello World", encoding="utf-8")

    result = runner.invoke(app, [str(markdown_file)])

    assert result.exit_code == 0
    assert "Hello World" in result.output


def test_missing_file_returns_error(tmp_path: Path) -> None:
    """A missing file produces an error."""
    markdown_file = tmp_path / "missing.md"

    result = runner.invoke(app, [str(markdown_file)])

    assert result.exit_code == 1


def test_non_markdown_file_returns_error(tmp_path: Path) -> None:
    """A file with an unsupported extension produces an error."""
    text_file = tmp_path / "example.txt"
    text_file.write_text("Hello World", encoding="utf-8")

    result = runner.invoke(app, [str(text_file)])

    assert result.exit_code == 1


def test_invalid_utf8_file_returns_error(tmp_path: Path) -> None:
    """A Markdown file containing invalid UTF-8 produces an error."""
    markdown_file = tmp_path / "invalid.md"
    markdown_file.write_bytes(b"\x80\x81\x82")

    result = runner.invoke(app, [str(markdown_file)])

    assert result.exit_code == 1
