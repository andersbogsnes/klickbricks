import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", type=str, help="Name to greet", default="World")
def hello(name: str):
    click.echo(f"Hello {name}")


if __name__ == '__main__':
    cli()
