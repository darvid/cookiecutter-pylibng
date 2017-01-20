"""Provides the {{cookiecutter.package_name}} command line interface."""
import click


@click.group()
@click.pass_context
def main(ctx):
    # type: (click.Context) -> None
    """{{cookiecutter.package_name}}: Frobnicates flux capacitors."""
