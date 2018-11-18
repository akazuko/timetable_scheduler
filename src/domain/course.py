class Course(object):
  def __init__(self, number, name, max_number_of_students, instructors):
    self.number = number
    self.name = name
    self.max_number_of_students = max_number_of_students
    self.instructors = instructors

  def __str__(self):
    return self.name
