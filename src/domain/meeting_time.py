class MeetingTime(object):
  def __init__(self, id, time):
    self.id = id
    self.time = time

  def __str__(self):
    return self.time