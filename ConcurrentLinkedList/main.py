from linked_list import LinkedList

ll = LinkedList()

ll.append(1233)
ll.delete("pos", pos=5)
ll.append(312)
ll.append(98127, "first")
ll.append(46712, "pos", pos=1)
ll.append(765)
print(ll.find(98127))
ll.print_list()

