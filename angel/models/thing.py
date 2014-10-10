from angel import api
import json

class Thing(object):
  def __init__(self, source_dict={}):
    self.source_dict = source_dict
    self.api = Thing.api()

  def __getattr__(self, key):
    value = self.source_dict[key]
    if isinstance(value, list) and all([isinstance(x, list) or isinstance(x, dict) for x in value]):
      return [Thing(x) for x in value]
    elif isinstance(value, dict):
      return Thing(value)
    else:
      return value

  def __str__(self):
    return str(self.source_dict)

  def __repr__(self):
    return self.__str__()

  @staticmethod
  def api():
    return api.AngelAPI()