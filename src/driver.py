import json
from os import sys, path

POPULATION_SIZE           = 9
MUTATION_RATE             = 0.1
CROSSOVER_RATE            = 0.9
TOURNAMENT_SELECTION_SIZE = 3
NUMB_OF_ELITE_SCHEDULES   = 1

def print_msg(msg):
  if isinstance(msg, dict):
    msg = json.dumps(msg, indent=2)
  
  print
  print "*" * 50
  print msg
  print "*" * 50

def print_data(data):
  print_msg("INPUT DATA INFORMATION")
  print_msg("Available departments")
  for dept in data.depts:
    _courses = [str(x) for x in dept.courses]
    print("name : %s, courses : %s" % (dept.name, _courses))
  
  print_msg("Available courses")
  for course in data.courses:
    _instructors = [str(x) for x in course.instructors]
    _msg = [
      "Course no.: %s, " % course.number,
      "Name: %s" % course.name,
      "Max no. of students: %s" % course.max_number_of_students,
      "Instructors: %s" % _instructors
    ]
    print(",".join(_msg))
    
  print_msg("Available rooms")
  for room in data.rooms:
    _msg = [
      "Room No: %s" % room.number,
      "Max seating capacity: %s" % room.seating_capacity
    ]
    print(",".join(_msg))

  print_msg("Available instructors")
  for instructor in data.instructors:
    _msg = [
      "ID: %s" % instructor.id,
      "Name: %s" % instructor.name
    ]
    print(",".join(_msg))
  
  print_msg("Available meeting times")
  for meeting_time in data.meeting_times:
    _msg = [
      "ID: %s" % meeting_time.id,
      "Meeting Time: %s" % meeting_time.time
    ]
    print(",".join(_msg))

if __name__ == '__main__' and __package__ is None:
  sys.path.insert(0, path.dirname(path.abspath(__file__)))
  from data import Data
  data = Data()
  print_data(data=data)
