import click

@click.group()
def main():
    "Update the maritime exchange data"
    pass

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def load(filename):
    """Print FILENAME if the file exists."""
    click.echo(click.format_filename(filename))

all_commands = [
    load
]

for cmd in all_commands:
    main.add_command(cmd)
