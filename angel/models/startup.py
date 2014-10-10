from thing import Thing

class Startup(Thing):

  @staticmethod
  def fetch_all():
    page, last_page = 1, 1
    while page <= last_page:
      response = Thing.api().get('startups', {'filter': 'raising', 'page': page})
      page, last_page = response.page, response.last_page
      yield response