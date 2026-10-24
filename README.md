# Markdown Viewer

A lightweight CLI tool to render Markdown files directly in the terminal, without needing an editor or browser.

## Installation

Requires [uv](https://docs.astral.sh/uv/).

Install directly from the repository (default branch: `main`):

```bash
uv tool install git+https://github.com/KleinMisha/md-cli.git
```


Install a specific branch 
```bash
uv tool install git+https://github.com/KleinMisha/md-cli.git@main
```

Install from a specific tag 
```bash
uv tool install git+https://github.com/KleinMisha/md-cli.git@v1.0.0
```

Once installed, the `md` command will be available in your terminal.

## Usage

Render a Markdown file:

```bash
md README.md
```

Display help:

```bash
md --help
```

## Requirements

- [ ] Accept a Markdown file path as a positional argument.
- [ ] Render Markdown directly in the terminal.
- [ ] Support common Markdown elements, including headings, lists, links, and code blocks.
- [ ] Display helpful usage information with `--help`.
- [ ] Report a clear error if the specified file does not exist or cannot be read.
- [ ] Return an appropriate exit code on success or failure.
- [ ] Include integration tests for the main CLI workflows.