from asyncio import Semaphore
from gender import Gender, get_gender_name
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


    def on_person_enter(self, person):
        self.bathroom.append(person)
        self.gender_using = person.gender

    def on_person_leave(self, person):
        self.bathroom.remove(person)
        if self.is_empty():
            self.gender_using = None

    def is_available(self, person):
        if self.is_full():
            return False
        elif self.gender_using == None:
            return True
        elif person.gender == Gender.female:
            return self.available_for_women()
        elif person.gender == Gender.male:
            return self.available_for_men()

    def available_for_women(self):
        if self.gender_using is None or self.gender_using == Gender.female:
            return True
        if self.gender_using == Gender.male and len(self.men_queue) == 0 \
        and self.is_empty():
            return True
        return False

    def available_for_men(self):
        if self.gender_using is None or self.gender_using == Gender.male:
            return True
        if self.gender_using == Gender.female and len(self.women_queue) == 0 \
        and self.is_empty():
            return True
        return False

    def is_enqueued(self, person):
        if person.gender == Gender.female:
            return person in self.women_queue
        elif person.gender == Gender.male:
            return person in self.men_queue
    
    def remove_from_queue(self, person):
        if person in self.women_queue:
            self.women_queue.remove(person)
        elif person in self.men_queue:
            self.men_queue.remove(person)

    def join_queue(self, person):
        if person.gender == Gender.female:
            self.women_queue.append(person)
        elif person.gender == Gender.male:
            self.men_queue.append(person)

    def get_next_person(self):
        if self.gender_using == Gender.female and len(self.women_queue) > 0:
            return True, self.women_queue[0]
        elif self.gender_using == Gender.male and len(self.men_queue) > 0:
            return True, self.men_queue[0]
        else:
            return False, None
            
    def is_full(self):
        return len(self.bathroom) >= self.capacity_max

    def is_empty(self):
        return len(self.bathroom) == 0

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
            print("Person " + str(i + 1) + ": " + str(id(val) % 1000000) + " " \
            + get_gender_name(val.gender))

