from linked_list import LinkedList
from threading import Thread

semaphore = thread.allocated_lock()

class FindThread (Thread):

    def __init__(self, linked_list):
        Thread.__init__(self)
        self.linked_list = linked_list

    def run(self, val):
        self.semaphore.acquire()
        self.linked_list.find(val)
