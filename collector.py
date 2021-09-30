from __future__ import annotations

import os
from typing import Optional

import click

from api import API


API_CHOICES = ('coinlib', 'rickandmorty', 'fortnitetracker')


@click.command()
@click.option('--api-name', '-a', help='Name of the API.', required=True,
              type=click.Choice(API_CHOICES, case_sensitive=False))
@click.option('--file', '-f', help='Path of the file to output the result.',
              type=click.Path(exists=False), required=True)
@click.option('--key', '-k', help='API key for the chosen API.',
              type=click.STRING)
def collector(api_name: str, file: os.PathLike | bytes, key: Optional[str]):
    api_instance = API(file, key)

    click.echo('Retrieving data from API...')
    if api_name == 'coinlib':
        api_instance.coinlib()

    elif api_name == 'rickandmorty':
        api_instance.rickandmorty()

    else:
        api_instance.fortnitetracker()
    click.echo(f'Saved API data to {file}!')


if __name__ == '__main__':
    collector()
