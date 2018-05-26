from threading import Thread, Lock
from gender import *
import threading
mutex = Lock()

class Bathroom_Control(object):

    def __init__(self, capacity):
        self.gender_using = None
        self.capacity_max = capacity
        self.usage = 0
        self.men_queue = list()
        self.women_queue = list()
        self.bathroom = list()


    def processMutex(intoBathroom):
      mutex.acquire()
      try:
        intoBathroom()
      finally:
        mutex.release()


    def join_queue(self, person):
        if person.gender == Gender.male:
            self.men_queue.append(person)
        elif person.gender == Gender.female:
            self.women_queue.append(person)
        else:
            raise RuntimeError("Gender of queued person not defined")

    def enter_bathroom(self, person):
        if person in self.men_queue:
            self.men_queue.remove(person)
        elif person in self.women_queue:
            self.women_queue.remove(person)

        self.processMutex(self.bathroom.append(person))
        self.usage += 1
        self.gender_using = person.gender
        person.start()
        self.print_status()

    def is_available(self, person):
        return self.usage < self.capacity_max and (self.gender_using == person.gender) or \
        self.gender_using is None

    def leave_bathroom(self, person):
        self.processMutex(self.bathroom.remove(person))
        self.usage -= 1
        self.check_next()

    def check_next(self):
        if self.usage < self.capacity_max:
            if len(self.men_queue) > 0 and (self.gender_using == Gender.male or \
            (self.gender_using == Gender.female and len(self.women_queue) == 0)):
              self.processMutex(self.enter_bathroom(self.men_queue[0]))

            elif len(self.women_queue) > 0 and (self.gender_using == Gender.female or \
            (self.gender_using == Gender.male and len(self.men_queue) == 0)):
              self.processMutex(self.enter_bathroom(self.women_queue[0]))


    def print_status(self):
        print('-----------------------------------------------------')
        print('BATHROOM STATUS')
        print('Actual gender:', get_gender_name(self.gender_using))
        print('Capacity:', self.capacity_max)
        print('Using:', self.usage)
        print('Men waiting:', len(self.men_queue))
        print('Women waiting:', len(self.women_queue))
        print('-----------------------------------------------------\n\n')
