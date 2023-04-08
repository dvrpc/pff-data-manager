import click
import psycopg2 as psql
from . import dataloader as army_corps

@click.group()
def main():
    "Interface for US Army Corps of Engineers Data"
    pass

@click.command()
@click.argument('path', type=click.Path(exists=True))
def load_tonnage(path):
    army_corps.load_tonnage(path)

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('table_name')
def insert_csv(path, table_name):
    army_corps.insert_csv(path, table_name)

all_commands = [
    load_tonnage,
    insert_csv,
]

for cmd in all_commands:
    main.add_command(cmd)