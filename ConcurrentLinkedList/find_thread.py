from linked_list import LinkedList
from threading import Thread
import random


class FindThread (Thread):

    def __init__(self, linked_list, id):
        Thread.__init__(self)
        self.linked_list = linked_list
        self.id = id

    def run(self):
        val = random.randint(0, 999999)
        print("Thread " + str(self.id) + ": Starting search for " + str(val))
        found = self.linked_list.find(val)
        if found:
            print("Thread " + str(self.id) + ": Found item " + str(val) + "!")
        else:
            print("Thread " + str(self.id) + ": Item " + str(val) + " not found!")