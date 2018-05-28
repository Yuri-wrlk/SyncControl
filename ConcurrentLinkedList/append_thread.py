from linked_list import LinkedList
from threading import Thread

class AppendThread (Thread):
    
    def __init__(self, linked_list):
        Thread.__init__(self)
        self.linked_list = linked_list

    def run(self, val, mode="last", pos="1"):
        self.linked_list.append(val, mode, pos)