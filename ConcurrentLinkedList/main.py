from linked_list import LinkedList
from append_thread import AppendThread
from delete_thread import DeleteThread
from find_thread import FindThread
from asyncio import Semaphore
import random
import time



def create_list():
    ll = LinkedList()
    for i in range(0, 100000):
        ll.append(random.randint(0, 99999))
    
    
    return ll


def create_threads(cap, ll, sem, count):
    thread_types = [random.randint(1,3) for i in range(0,cap)]
    for i in thread_types:
        if i == 1:
            thread = AppendThread(ll, sem, count)
            thread.start()
        if i == 2:
            thread = DeleteThread(ll, sem, count)
            thread.start()
        if i == 3:
            thread = FindThread(ll, count)
            thread.start()
        
        count += 1
    
    

    return count


if(__name__ == "__main__"):
    ll = create_list()
    sem = Semaphore()
    count = 1
    while True:
        count = create_threads(5, ll, sem, count)
        print("------------------------------------------------------")
        time.sleep(0.2)

    

