from angel import api
import json

class Thing(object):
  def __init__(self, source_dict={}):
    self.source_dict = source_dict
    self.api = Thing.api()

  def __getattr__(self, key):
    try:
      value = self.source_dict[key]
    except:
      return super(Thing, self).__getattr__(key)
    if type(value) is list:
      return [Thing(x) for x in value]
    elif type(value) is dict:
      return Thing(value)
    else:
      return value

  def __str__(self):
    return json.dumps(self.source_dict, sort_keys=True, indent=4, separators=(',', ': '))

  def __repr__(self):
    return self.__str__()

  @staticmethod
  def api():
    return api.AngelAPI()