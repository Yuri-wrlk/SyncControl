from asyncio import Semaphore
from gender import *
import threading

class Bathroom_Control(object):

    def __init__(self, capacity):
        self.gender_using = None
        self.capacity_max = capacity
        self.usage = 0
        self.men_queue = list()
        self.women_queue = list()
        self.bathroom = list()
        self.semaphore = Semaphore(value=capacity)


    def get_semaphore(self):
        return self.semaphore

    def print_status(self):
        print('-----------------------------------------------------')
        print('BATHROOM STATUS')
        print('Actual gender:', get_gender_name(self.gender_using))
        print('Capacity:', self.capacity_max)
        print('Using:', len(self.bathroom))
        print('Men waiting:', len(self.men_queue))
        print('Women waiting:', len(self.women_queue))
        print('-----------------------------------------------------\n')
        print("People inside:")
        for i, val in enumerate(self.bathroom):
            print("Person " + str(i) + ": " + str(id(val) % 100000))


'''
def processMutex(self, person):
        mutex.acquire()
        try:
            self.enter_bathroom(person)
        finally:
            mutex.release()


    def join_queue(self, person):
        if person.gender == Gender.male:
            self.men_queue.append(person)
        elif person.gender == Gender.female:
            self.women_queue.append(person)
        else:
            raise RuntimeError("Gender of queued person not defined")

    def try_enter_bathroom(self, person):
        if person.gender == Gender.female and self.available_for_women() \
        or person.gender == Gender.male and self.available_for_men():
            self.enter_bathroom(person)
        else:
            self.join_queue(person)
        

    def enter_bathroom(self, person):
        self.bathroom.append(person)
        self.gender_using = person.gender
        person.start()

    def is_available(self, person):
        return len(self.bathroom) < self.capacity_max and (self.gender_using == person.gender) or \
        self.gender_using is None

    def leave_bathroom(self, person):
        self.bathroom.remove(person)
        self.check_next()

    def check_next(self):
        if len(self.bathroom) < self.capacity_max:
            if self.available_for_women():
                self.processMutex(self.men_queue[0])
            elif self.available_for_men():
                self.processMutex(self.women_queue[0])


    def available_for_men(self):
        if self.gender_using is None or self.gender_using == Gender.male:
            return True
        if self.gender_using == Gender.female and len(self.women_queue) == 0:
            return True
        return False

    def available_for_women(self):
        if self.gender_using is None or self.gender_using == Gender.female:
            return True
        if self.gender_using == Gender.male and len(self.men_queue) == 0:
            return True
        return False
'''