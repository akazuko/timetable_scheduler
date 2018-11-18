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
    room1 = Room(number=1, seating_capacity=100)
    room2 = Room(number=2, seating_capacity=100)
    self.rooms = [room1, room2]

    # create meeting times
    meeting_time1 = MeetingTime(id="MT1", time="MWF 09:00 - 10:00")
    meeting_time2 = MeetingTime(id="MT2", time="MWF 10:00 - 11:00")
    meeting_time3 = MeetingTime(id="MT3", time="MWF 11:00 - 12:00")
    meeting_time4 = MeetingTime(id="MT4", time="MWF 12:00 - 13:00")

    meeting_time5 = MeetingTime(id="MT5", time="TTH 09:00 - 10:00")
    meeting_time6 = MeetingTime(id="MT6", time="TTH 10:00 - 11:00")
    meeting_time7 = MeetingTime(id="MT7", time="TTH 11:00 - 12:00")
    meeting_time8 = MeetingTime(id="MT8", time="TTH 12:00 - 13:00")

    self.meeting_times = [
      meeting_time1, 
      meeting_time2, 
      meeting_time3, 
      meeting_time4, 
      meeting_time5, 
      meeting_time6, 
      meeting_time7, 
      meeting_time8
    ]

    # creating instructors
    instructor1 = Instructor(id="I1", name="ALGO teacher")
    instructor2 = Instructor(id="I2", name="IS teacher")
    instructor3 = Instructor(id="I3", name="DBMS teacher")
    instructor4 = Instructor(id="I4", name="CI teacher")
    instructor5 = Instructor(id="I5", name="AI teacher")

    self.instructors = [instructor1, instructor2, instructor3, instructor4, instructor5]

    # create courses
    course1 = Course(number="C1", name="ALGO", max_number_of_students=100, instructors=[instructor1])
    course2 = Course(number="C2", name="IS", max_number_of_students=100, instructors=[instructor2])
    course3 = Course(number="C3", name="DBMS", max_number_of_students=100, instructors=[instructor3])
    course4 = Course(number="C4", name="CI", max_number_of_students=100, instructors=[instructor4])
    course5 = Course(number="C5", name="AI", max_number_of_students=100, instructors=[instructor5])

    self.courses = [course1, course2, course3, course4, course5]

    # create departments
    department1 = Department(name="MSC", courses=list(self.courses))
    department2 = Department(name="MCA", courses=list(self.courses))

    self.depts = [department1, department2]

    # define the number of classes
    self.number_of_classes = sum([len(x.courses) for x in self.depts])
