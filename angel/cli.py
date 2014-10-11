from models import *
import json, datetime

try:
  import click
except:
  raise Exception("Run `pip install -r requirements.txt` to continue.")

@click.command()
@click.argument('input', envvar='ANGEL_FILE', type=click.File('r'))
@click.option('--pretty/--no-pretty', default=True, help='Pretty print output.')
def find_companies(input, pretty):
  start = datetime.datetime.now()
  candidate = person.Person(json.load(input))
  progressbar_length = startup.Startup.num_pages()/(len(candidate.interests) or 1)
  
  if pretty:
    click.clear()
    click.echo(click.style('Welcome to angel!', fg='green'))
    click.echo(click.style('I will now search AngelList for this candidates optimal companies.', fg='green'))
    click.echo('\n')
    with click.progressbar(startup.Startup.fetch_all(), length=progressbar_length) as all_startups:
      results = get_results(all_startups, candidate, start)
      click.echo('\n\n')
      seconds_elapsed = (datetime.datetime.now() - start).seconds
      click.echo(click.style('I found {num} results in {secs} seconds!'.format(num=len(results), secs=seconds_elapsed), fg='green'))
      click.echo('\n')
      click.echo(json.dumps(results, sort_keys=True, indent=2, separators=(',', ': ')))
  else:
    click.echo(json.dumps(get_results(startup.Startup.fetch_all(), candidate, start)))

def get_results(all_startups, candidate, start):
  results = []
  for company in all_startups:
      for market in company.markets:
        if (not candidate.cleaned_interests) or market.name.strip().lower() in candidate.cleaned_interests:
          if not candidate.would_relocate and not any([x in candidate.cleaned_locations for x in company.cleaned_locations]):
            continue
          if candidate.must_have_opening:
            if not company.jobs():
              continue
            if candidate.full_time_only and not any([x.job_type == 'full-time' for x in company.jobs()]):
              continue
          results.append(company.summarize())
          break
      if len(results) == 10 or datetime.datetime.now() - start > datetime.timedelta(minutes=5):
        break
  return results