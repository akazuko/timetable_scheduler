class Instructor(object):
  def __init__(self, id, name):
    self.id = id
    self.name = name
  
  def __str__(self):
    return self.name
  
  def __eq__(self, other):
    if isinstance(other, Instructor):
      return self.id == other.id
    
    return self == other