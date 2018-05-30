from bathroom_control import Bathroom_Control
from person import Person
from gender import Gender
import random
import time
import os
import sys

def get_random_gender():
    bin_val = random.randint(0,1)
    if bin_val == 0:
        return Gender.male
    else:
        return Gender.female
    

if(__name__ == "__main__"):
    if len(sys.argv) > 1 and int(sys.argv[1]):
        capacity = int(sys.argv[1])
    else:
        capacity = 5
    controller = Bathroom_Control(capacity)
    controller.print_status()
    counter = 1
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n\nStep " + str(counter))    
        new_person = Person(get_random_gender(), random.randint(1, 4), controller)
        new_person.try_enter_bathroom()
        people_waiting, queued_person = controller.get_next_person()
        if people_waiting:
            queued_person.try_enter_bathroom()
        controller.print_status()
        counter += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        