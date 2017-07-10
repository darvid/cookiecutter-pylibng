"""Provides the {{cookiecutter.package_name}} command line interface."""
from __future__ import absolute_import

import click


@click.group()
@click.pass_context
def main(ctx):
    # type: (click.Context) -> None
    """{{cookiecutter.package_name}}: {{cookiecutter.project_short_description}}"""
