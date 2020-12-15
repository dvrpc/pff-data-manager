import click
import psycopg2 as psql
from .dataloader import get_trade

@click.group()
def main():
    "Interface for all US Census International Trade data"
    pass

@click.command()
@click.argument('year')
def load(year):
    """Query USA Trade API for year of interest"""
    
    click.echo("Downloading trade data for %s" % year) 
    get_trade(year)

    # click.echo(response.text)

all_commands = [
    load
]

for cmd in all_commands:
    main.add_command(cmd)