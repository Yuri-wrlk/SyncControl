from linked_list import LinkedList
from threading import Thread
from asyncio import Semaphore
import random

class AppendThread (Thread):

    def __init__(self, linked_list, sem_a, id):
        Thread.__init__(self)
        self.linked_list = linked_list
        self.sem_a = sem_a
        self.id = id

    def run(self, mode="last", pos="1"):
        rand_pos = random.randint(0, 10000)
        print("Thread " + str(self.id) + ": Starting insertion at position " + str(rand_pos))
        self.sem_a.acquire()
        self.linked_list.append(random.randint(0, 999999), mode="pos", pos=rand_pos)
        self.sem_a.release()
        print("Thread " + str(self.id) + ": Item fully inserted at position" + str(rand_pos) + "!")
        
