import os, models.thing

try:
  import requests
except:
  raise Exception("Run `pip install -r requirements.txt` to continue.")

class AngelAPI:
  def __init__(self, access_token=os.getenv('ANGEL_ACCESS_TOKEN')):
    self.endpoint = 'https://api.angel.co/1/'
    self.access_token = access_token
    if not access_token:
      raise Exception("Set the ANGEL_ACCESS_TOKEN environment variable to continue.")

  def make_request(self, verb, action, query_params):
    query_params.update({'access_token': self.access_token})
    json = getattr(requests, verb)('{endpoint}{action}'.format(endpoint=self.endpoint, action=action), params=query_params).json()
    return models.thing.Thing(json)

  def get(self, action, query_params={}):
    return self.make_request('get', action, query_params)

  def post(self, action, query_params={}):
    return self.make_request('post', action, query_params)