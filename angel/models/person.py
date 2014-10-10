from thing import Thing

class Person(Thing):

  def cleaned_interests(self):
    return [str(x).strip().lower() for x in self.interests]