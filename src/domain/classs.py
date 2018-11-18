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
      'department': self.department,
      'course': self.course,
      'room': self.room,
      'instructor': self.instructor,
      'meeting_time': self.meeting_time
    }
    return _fmt.format(**args)
