from typer import Exit, Typer, echo

app = Typer(no_args_is_help=True)


@app.command()
def hello() -> None:
    echo("Welcome to md-cli!")
    raise Exit(code=0)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
