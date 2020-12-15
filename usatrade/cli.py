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

all_commands = [
    load
]

for cmd in all_commands:
    main.add_command(cmd)