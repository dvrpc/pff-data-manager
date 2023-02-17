import click
import psycopg2 as psql
from . import dataloader as usatrade

@click.group()
def main():
    "Interface for all US Census International Trade data"
    pass

@click.command()
@click.argument('table')
@click.option('--year','-y', help='Specify year for annual_trade table')
def get(table, year):
    if table == "annual_trade":
        click.echo(usatrade.get_annual_trade(year))

@click.command()
@click.argument('table')
@click.option('--year','-y', help='Specify year for annual_trade table')
def insert(table, year):
    if table == "annual_trade":
        usatrade.insert_annual_trade(usatrade.get_annual_trade(year))

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