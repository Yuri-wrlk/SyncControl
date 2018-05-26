from enum import Enum
from gender import *
from threading import Thread
from bathroom_control import Bathroom_Control
import time
import sys

class Person(Thread):

    def __init__(self, gender, time_spent, bathroom_control):
        Thread.__init__(self)
        self.gender = gender
        self.time_spent = time_spent
        self.bathroom_control = bathroom_control
        self.print_person()

    def run(self):
        start_time = time.clock()
        while time.clock() - start_time < self.time_spent:
            time.sleep(0.0005)
        self.bathroom_control.leave_bathroom(self)

    def print_person(self):
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('New person created!')
        print('Person ID:', id(self))
        print('Gender:', get_gender_name(self.gender))
        print('Time to spend:', self.time_spent)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
