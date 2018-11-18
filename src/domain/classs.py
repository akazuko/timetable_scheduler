class Class(object):
  def __init__(self, id, department, course):
    self.id = id
    self.department = department
    self.course = course
    self.room = None
    self.instructor = None
    self.meeting_time = None

  def __str__(self):
    _fmt = '[{department},{course},{room},{instructor},{meeting_time}]'
    args = {
      'department': str(self.department),
      'course': str(self.course),
      'room': str(self.room),
      'instructor': str(self.instructor),
      'meeting_time': str(self.meeting_time)
    }
    return _fmt.format(**args)
