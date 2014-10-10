from thing import Thing
import itertools

class Person(Thing):

  @property
  def cleaned_interests(self):
    return [x.strip().lower() for x in self.interests]

  @property
  def cleaned_locations(self):
    locations = [x.split(',') + [x] for x in self.locations]
    return list(set(itertools.chain(*[[x.strip().lower() for x in loc] for loc in locations])))