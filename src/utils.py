import json
from random import random, seed
from tabulate import tabulate

def get_random_number():
  seed()
  return random()

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

def print_population_schedules(population, generation_number):
  _schedule_number = 0
  
  print_msg("Generation Number: %s" % generation_number)
  print
  print

  _schedules = []
  for x in population.schedules:
    _schedules.append([
      _schedule_number,
      str(x),
      x.fitness,
      x.number_of_conflicts
    ])
    _schedule_number += 1

  headers = [
    "Schedule #", 
    "Classes [dept, class, room, instructor, meeting-time]", 
    "Fitness", 
    "Conflicts"
  ]

  print(tabulate(_schedules, headers=headers))

def print_schedule_as_table(data, schedule, generation):
  _class_number = 1
  
  _classes = schedule.classes
  _headers = [
    "Class #",
    "Dept",
    "Course (number, max # of students)",
    "Room (capacity)",
    "Instructor (Id)",
    "Meeting Time"
  ]

  table_data = []
  for _class in _classes:
    major_idx = -1
    for idx, _dept in enumerate(data.depts):
      if _dept.name == _class.department.name:
        major_idx = idx

    course_idx = -1
    for idx, _course in enumerate(data.courses):
      if _course.name == _class.course.name:
        course_idx = idx
    
    room_idx = -1
    for idx, _room in enumerate(data.rooms):
      if _room.number == _class.room.number:
        room_idx = idx
    
    instructor_idx = -1
    for idx, _instructor in enumerate(data.instructors):
      if _instructor.id == _class.instructor.id:
        instructor_idx = idx 
    
    meeting_time_idx = -1
    for idx, _meeting_time in enumerate(data.meeting_times):
      if _meeting_time.id == _class.meeting_time.id:
        meeting_time_idx = idx

    table_data.append([
      _class_number,
      data.depts[major_idx].name,
      "%s (%s, %s)" % (data.courses[course_idx].name, data.courses[course_idx].number, _class.course.max_number_of_students),
      "%s (%s)" % (data.rooms[room_idx].number, _class.room.seating_capacity),
      "%s (%s)" % (data.instructors[instructor_idx].name, data.instructors[instructor_idx].id),
      "%s (%s)" % (data.meeting_times[meeting_time_idx].time, data.meeting_times[meeting_time_idx].id)
    ])
    _class_number += 1

  print
  print(tabulate(table_data, headers=_headers))
  print

  if schedule.fitness == 1.0:
    print_msg("Solution Found in %s generations" % (generation + 1))
