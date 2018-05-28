from linked_list import LinkedList
from threading import Thread

class DeleteThread (Thread):
    
    def __init__(self, linked_list):
        Thread.__init__(self)
        self.linked_list = linked_list

    def run(self, val, mode="last", pos="1"):
        self.linked_list.delete(val, mode, pos)