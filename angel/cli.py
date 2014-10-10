from models import *
import click, json

@click.command()
@click.argument('input', envvar='ANGEL_FILE', type=click.File('r'))
@click.option('--pretty/--no-pretty', default=True, help='Pretty print output.')
def find_companies(input, pretty):
  click.clear()
  click.echo(click.style('Welcome to angel!', fg='green'))
  click.echo(click.style('I will now search AngelList for this candidates optimal companies.', fg='green'))
  click.echo('\n')
  results = []
  candidate = person.Person(json.load(input))
  progressbar_length = startup.Startup.num_pages()/(25*len(candidate.interests))
  with click.progressbar(startup.Startup.fetch_all(), length=progressbar_length) as all_startups:
    for company in all_startups:
      for market in company.markets:
        if market.name.strip().lower() in candidate.cleaned_interests():
          results.append(company.summarize())
          break
      if len(results) == 10:
        break
    click.echo('\n\n')
    click.echo(click.style('I found {num} results!'.format(num=len(results)), fg='green'))
    click.echo('\n')
    if pretty:
      click.echo(json.dumps(results, sort_keys=True, indent=2, separators=(',', ': ')))
    else:
      click.echo(json.dumps(results))