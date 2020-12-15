import click

@click.group()
def main():
    "Update the maritime exchange data"
    pass

@click.command()
def say_hi():
    print("What the fuck is up asshat")

all_commands = [
    say_hi
]

for cmd in all_commands:
    main.add_command(cmd)
