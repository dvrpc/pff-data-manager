import click
import psycopg2 as psql
from .dataloader import get_trade, check_year


@click.group()
def main():
    "Interface for US Census International Trade data"
    pass


@click.command()
@click.argument("year", type=int)
@click.option("--multi", "-m", help="Specify a year ending for range of years", type=int)
def load(year: int, multi: int):
    """Import new USA Trade data for DVRPC ports 
    
    Specify year of data
    """
    years = list(range(year, multi + 1)) if multi else [year]
    for period in years:
        # run a check of year on current database
        status = check_year(period)
        if status == "exists":
            click.echo(f"Process failed. The data for {period} already exists in the database")

        else:
            click.echo(f"Downloading trade data for {period}")
            get_trade(period)


@click.command()
@click.argument("imex")
@click.argument("year")
@click.option("--port", "-p", default="", help="Specify a US Census Port ID")
@click.option("--number", "-n", default=5, help="Specify top n results")
def top(imex, year, port, number):
    """Query top commodities by direction and year"""

    click.echo("%s for %s" % (port, number))


all_commands = [load, top]

for cmd in all_commands:
    main.add_command(cmd)
