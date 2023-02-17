import click
import psycopg2 as psql
from .dataloader import get_annual_trade, insert_annual_trade 

@click.group()
def main():
    "Interface for all US Census International Trade data"
    pass

@click.command()
@click.argument('year')
def get(year):
    click.echo(get_annual_trade(year))

@click.command()
@click.argument('year')
def insert(year):
    insert_annual_trade(get_annual_trade(year))

@click.command()
@click.argument('imex')
@click.argument('year')
@click.option('--port', '-p', default='', help='Specify a US Census Port ID')
@click.option('--number', '-n', default=5, help='Specify top n results')
def top(imex, year, port, number):
    """Query top commodities by direction and year"""
    
    click.echo('%s for %s' % (port, number))

all_commands = [
    get,
    insert
]

for cmd in all_commands:
    main.add_command(cmd)