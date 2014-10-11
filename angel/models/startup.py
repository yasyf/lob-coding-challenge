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
    summary = {k:getattr(self, k) for k in properties}
    summary['jobs'] = []
    for job in self.jobs():
      location = [x for x in job.tags if x.tag_type == 'LocationTag'][0]
      summary['jobs'].append({'location': location.display_name, 'title': job.title, 'salary': job.salary_max})
    return summary

  @property
  def cleaned_locations(self):
    return [x.name.strip().lower() for x in self.locations]

  @property
  def cities(self):
    return [x.display_name for x in self.locations]

  def jobs(self):
    try:
      return self._jobs
    except:
      self._jobs = [Thing(x) for x in self.api.get('startups/{id}/jobs'.format(id=self.id))]
      return self._jobs
  