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
        print('New person created!')
        self.print_person()
        self.semaphore = self.bathroom_control.get_semaphore()

    def run(self):
        if self.bathroom_control.is_available():
            self.semaphore.acquire()
            print(str(id(self)) + ": entrei no banheiro!")
            start_time = time.clock()
            while time.clock() - start_time < self.time_spent:
                time.sleep(0.005)

            self.semaphore.release()
            print(str(id(self)) + ": saí do banheiro!")
            self.bathroom_control.leave_bathroom(self)


    def print_person(self):
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Person ID:', id(self))
        print('Gender:', get_gender_name(self.gender))
        print('Time to spend:', self.time_spent)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
