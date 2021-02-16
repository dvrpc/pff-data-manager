import click
import psycopg2 as psql
from .dataloader import get_trade, check_year

@click.group()
def main():
    "Interface for all US Census International Trade data"
    pass

@click.command()
@click.argument('year')
def load(year):
    """Import new USA Trade data for DVRPC ports 
    
    Specify year of data
    """
    # run a check of year on current database
    status = check_year(year)
    if status == 'exists':
        click.echo('Process failed. The data for %s already exists in the database' % year)
        
    else:
        click.echo("Downloading trade data for %s" % year) 
        get_trade(year)

@click.command()
@click.argument('imex')
@click.argument('year')
@click.option('--port', '-p', default='', help='Specify a US Census Port ID')
@click.option('--number', '-n', default=5, help='Specify top n results')
def top(imex, year, port, number):
    """Query top commodities by direction and year"""
    
    click.echo('%s for %s' % (port, number))

all_commands = [
    load,
    top
]

for cmd in all_commands:
    main.add_command(cmd)