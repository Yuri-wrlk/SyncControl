from bathroom_control import Bathroom_Control
from person import Person
from gender import Gender
import random
import time
import os

def get_random_gender():
    bin_val = random.randint(0,1)
    if bin_val == 0:
        return Gender.male
    else:
        return Gender.female
    

if(__name__ == "__main__"):
    
    controller = Bathroom_Control(10)
    controller.print_status()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
            
        new_person = Person(get_random_gender(), random.randint(1, 4), controller)
        new_person.try_enter_bathroom()
        people_waiting, queued_person = controller.get_next_person()
        if people_waiting:
            queued_person.try_enter_bathroom()
        controller.print_status()
        time.sleep(2)
        