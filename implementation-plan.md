# Implementation Plan

## 1. Set Up Project

- [ ] Initialize the project: `uv init --project md-cli`
- [ ] Rename `src/md_cli` to `src/md`
- [ ] Add `__init__.py` files where needed to define Python packages.
- [ ] Configure `pyproject.toml` to package `md` and expose a CLI command named `md`.
- [ ] Install `typer` and `rich` as runtime dependencies.
- [ ] Add `pytest` as a development dependency.
- [ ] Verify that the project installs correctly and the CLI command is available.

## 2. Business Logic

- [ ] Create `src/md/core/render_markdown.py`.
- [ ] Implement a `render_markdown()` function that reads a Markdown file and renders it using Rich's `Markdown` class and `Console`.
- [ ] Raise `FileNotFoundError` if the specified file does not exist.
- [ ] Handle other relevant errors, such as file access errors and invalid UTF-8 content, where appropriate.
- [ ] Keep the rendering logic minimal; rely on Rich for Markdown parsing and rendering.
- [ ] No dedicated unit tests for now: the rendering functionality is delegated to Rich, and file handling relies on standard Python functionality.

## 3. CLI

- [ ] Create `src/md/cli/entrypoint.py`.
- [ ] Instantiate the Typer application.
- [ ] Configure the default help output, including usage information and command descriptions.
- [ ] Define a command directly under the `md` executable that accepts a Markdown file path.
- [ ] Delegate rendering to the `render_markdown()` function defined in the business logic.
- [ ] Validate user input and provide clear error messages for missing files or invalid paths.
- [ ] Ensure the CLI exits with an appropriate status code on failure.
- [ ] **Optional:** Define command groups in separate Python modules and register them with the main Typer application if the CLI grows.

## 4. Integration Tests

- [ ] Create `tests/integration/`.
- [ ] Test rendering an existing Markdown file through the CLI.
- [ ] Test behavior when the specified file does not exist.
- [ ] Test behavior when the Markdown file cannot be read.
- [ ] Verify that successful execution returns exit code `0`.
- [ ] Verify that failures return a non-zero exit code.
- [ ] Keep tests focused on critical application workflows rather than Rich's internal rendering behavior.

## 5. Final Verification

- [ ] Run the test suite with `pytest`.
- [ ] Install the project in editable mode using `uv pip install -e .` or the appropriate `uv` project workflow.
- [ ] Verify that `md --help` displays the CLI help.
- [ ] Verify that `md README.md` renders a Markdown file directly in the terminal.
- [ ] Verify that the CLI works when invoked from outside the project directory.