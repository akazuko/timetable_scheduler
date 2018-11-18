from domain import (
  Class,
  Course,
  Department,
  Instructor,
  MeetingTime,
  Room
)

class Data(object):
  def __init__(self):
    self.rooms = None
    self.instructors = None
    self.courses = None
    self.depts = None
    self.meeting_times = None
    self.number_of_classes = None

    self.initialize()
  
  def initialize(self):
    # create rooms
    room1 = Room(number="R1", seating_capacity=25)
    room2 = Room(number="R2", seating_capacity=45)
    room3 = Room(number="R3", seating_capacity=35)
    self.rooms = [room1, room2, room3]

    # create meeting times
    meeting_time1 = MeetingTime(id="MT1", time="MWF 09:00 - 10:00")
    meeting_time2 = MeetingTime(id="MT2", time="MWF 10:00 - 11:00")
    meeting_time3 = MeetingTime(id="MT3", time="TTH 09:00 - 10:00")
    meeting_time4 = MeetingTime(id="MT4", time="TTH 10:00 - 11:00")

    self.meeting_times = [
      meeting_time1, 
      meeting_time2, 
      meeting_time3, 
      meeting_time4
    ]

    # creating instructors
    instructor1 = Instructor(id="I1", name="ALGO teacher")
    instructor2 = Instructor(id="I2", name="IS teacher")
    instructor3 = Instructor(id="I3", name="DBMS teacher")
    instructor4 = Instructor(id="I4", name="CI teacher")

    self.instructors = [instructor1, instructor2, instructor3, instructor4]

    # create courses
    course1 = Course(number="C1", name="ALGO", max_number_of_students=25, instructors=[instructor1, instructor2])
    course2 = Course(number="C2", name="IS", max_number_of_students=35, instructors=[instructor1, instructor2, instructor3])
    course3 = Course(number="C3", name="DBMS", max_number_of_students=25, instructors=[instructor1, instructor2])
    course4 = Course(number="C4", name="CI", max_number_of_students=30, instructors=[instructor3, instructor4])
    course5 = Course(number="C5", name="AI", max_number_of_students=35, instructors=[instructor4])
    course6 = Course(number="C6", name="DATA_MINING", max_number_of_students=45, instructors=[instructor1, instructor3])
    course7 = Course(number="C7", name="NETWORKS", max_number_of_students=45, instructors=[instructor2, instructor4])

    self.courses = [course1, course2, course3, course4, course5, course6, course7]

    # create departments
    department1 = Department(name="MSC", courses=[course1, course3])
    department2 = Department(name="MCA", courses=[course2, course4, course5])
    department3 = Department(name="BSC", courses=[course6, course7])

    self.depts = [department1, department2, department3]

    # define the number of classes
    self.number_of_classes = sum([len(x.courses) for x in self.depts])
