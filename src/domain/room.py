class Room(object):
  def __init__(self, number, seating_capacity):
    self.number = number
    self.seating_capacity = seating_capacity

  def __str__(self):
    return self.number
    
  def __eq__(self, other):
    if isinstance(other, Room):
      return self.number == other.number
    
    return self == other