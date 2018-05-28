from linked_list import LinkedList
from threading import Thread

class FindThread (Thread):
    
    def __init__(self, linked_list):
        Thread.__init__(self)
        self.linked_list = linked_list

    def run(self, val):
        self.linked_list.find(val)