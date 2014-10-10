from models import *
import click, json

@click.command()
@click.argument('input', envvar='ANGEL_FILE', type=click.File('r'))
def find_companies(input):
  person = json.load(input)
  click.echo(person)