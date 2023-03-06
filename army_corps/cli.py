import click
import psycopg2 as psql
from . import dataloader as army_corps

@click.group()
def main():
    "Interface for US Army Corps of Engineers Data"
    pass

@click.command()
@click.argument('folderPath')
@click.option('--overwrite')
def load_tonnage(folderPath, overwrite):
    army_corps.load_tonnage(folderPath, overwrite)

def load_principal_ports():
    army_corps.load_principal_ports()

def load_dvrpc_port_names(filePath):
    army_corps.load_dvrpc_port_names(filePath)

all_commands = [
    load_tonnage,
    load_principal_ports,
    load_dvrpc_port_names
]

for cmd in all_commands:
    main.add_command(cmd)