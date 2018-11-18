class Department(object):
  def __init__(self, name, courses):
    self.name = name
    self.courses = courses

  def __str__(self):
    return self.name
