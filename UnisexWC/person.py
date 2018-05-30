from enum import Enum
from gender import Gender, get_gender_name
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

    def run(self):
        
        print(str(id(self)) + ": I entered the bathroom!")
        start_time = time.time()
        while time.time() - start_time < self.time_spent:
            time.sleep(0.002)

        self.bathroom_control.on_person_leave(self)
        print(str(id(self)) + ": I left the bathroom!")
        

    def try_enter_bathroom(self):
        if self.bathroom_control.is_available(self):
            if self.bathroom_control.is_enqueued(self):
                self.bathroom_control.remove_from_queue(self)
            self.bathroom_control.on_person_enter(self)
            self.start()
        else:
            self.bathroom_control.join_queue(self)

    def print_person(self):
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Person ID:', id(self))
        print('Gender:', get_gender_name(self.gender))
        print('Time to spend:', self.time_spent)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
