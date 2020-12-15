import click
import psycopg2 as psql

from utils.settings import conn_string
from .dataloader import get_imports

@click.group()
def main():
    "Interface for all US Census International Trade data"
    pass

@click.command()
@click.argument('year')
def load(year):
    """Query USA Trade API for year of interest"""
    
    click.echo("Downloading export data for %s" % year) 
    get_imports(year)

    # click.echo(response.text)

all_commands = [
    load
]

for cmd in all_commands:
    main.add_command(cmd)