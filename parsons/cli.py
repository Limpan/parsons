# -*- coding: utf-8 -*-
"""


"""
import click


@click.group()
def cli():  # NOQA
    pass


@cli.command()
def generate_problem():
    pass
