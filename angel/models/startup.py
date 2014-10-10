from thing import Thing

class Startup(Thing):

  @staticmethod
  def fetch_all(page=1):
    page, last_page = page, Startup.num_pages()
    while page <= last_page:
      response = Thing.api().get('startups', {'filter': 'raising', 'page': page})
      page = response['page'] + 1
      for startup in response['startups']:
        yield Startup(startup)

  @staticmethod
  def num_pages():
    return Thing.api().get('startups', {'filter': 'raising', 'per_page': 1})['last_page']

  def summarize(self):
    properties = ['name', 'quality', 'high_concept', 'company_url', 'angellist_url', 'cities']
    return {k:getattr(self, k) for k in properties}

  @property
  def cleaned_locations(self):
    return [x.name.strip().lower() for x in self.locations]

  @property
  def cities(self):
    return [x.name.title() for x in self.locations]
  