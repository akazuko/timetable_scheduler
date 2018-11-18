# Scheduling TimeTable using Genetic Algorithm

***

The idea is to leverage the power of Genetic Algorithm to solve timetable scheduling problem.

# Steps to install

Inside your virtual environment, simply do:
```
pip install -r requirements.txt
```

# Organization of the code ( inside src )

* data.py : Placeholder where data to be scheduled is kept. 
  Now this is basically acting as the store where the data in 
  the required format from any source can be loaded.

* driver.py : Primary driver we use to prepare the timetable.

* genetic_algorithm.py : Placeholder for the Genetic Algorithm.

* populaton.py : Definition of a population is kept here

* schedule.py : Definition of a schedule is kept here

* utils.py : Few utility functions to facilitate better code organization

* domain/ : The entities we are working with while defining a schedule

    * class : (department, course, instructor, meeting_time, room)
    * course : (name, max_number_of_students,instructors) 
    * department : (name, courses)
    * instructor : (name)
    * meeting_time : (time)
    * room : (number, seating_capacity)

# Steps to run the code

Once you have the virtual env activated, do the following:
```
cd src && python driver.py
```
