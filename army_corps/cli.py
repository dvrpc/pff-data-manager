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
def load_principal_ports():
    army_corps.load_principal_ports()

@click.command()
@click.argument('path')
def load_dvrpc_port_names(path):
    army_corps.load_dvrpc_port_names(path)

all_commands = [
    load_tonnage,
    load_principal_ports,
    load_dvrpc_port_names
]

for cmd in all_commands:
    main.add_command(cmd)