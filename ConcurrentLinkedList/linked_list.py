from node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = self.head

    def find (self, val):
        current = self.head
        while current != None:
            if current.val == val:
                return True, current
            current = current.next
        else:
            return False, None        
        

    def append(self, val, mode="last", pos=1):
        worker = Node(val)
        # Regardless of the mode, if the list is empty then start a new one
        if self.head == None:
            self.head = worker
            self.tail = worker
        else:
            if mode == "first" or (mode == "pos" and pos == 1):
                self.__append_first(worker)
            elif mode == "last":
                self.__append_last(worker)
            elif mode == "pos":
                self.__append_pos(worker, pos)
                
    def __append_first(self, worker):
        worker.next = self.head
        self.head = worker

    def __append_last(self, worker):
        self.tail.next = worker
        self.tail = worker
    
    def __append_pos(self, worker, pos):
        current = self.head
        pre = Node(None)
        for i in range(1, pos):
            pre = current
            if current.next != None:
                current = current.next
        if current == self.head:
            self.__append_first("first")
            return
        if current == self.tail:
            self.__append_last(worker)
            return
        pre.next = worker
        worker.next = current
        

    def delete(self, mode="last", pos=1):
        # Skips method if the list is empty
        if self.head == None:
            return

        elif mode == "first":
            self.__delete_first()
        elif mode == "last":
            self.__delete_last()
        elif mode == "pos":
            self.__delete_pos(pos)
            

    def __delete_first(self):
        # Removes first element and adjusts head
        temp = self.head
        if self.head.next == None:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
        del temp

    def __delete_last(self):
        # Removes last element and adjusts tail
        current = self.head
        pre = None
        # Must go through the list to find previous node to the tail
        while current.next != None:
            pre = current
            current = current.next
        if pre == None:
            self.head = None
            self.tail = self.head
        else:
            self.tail = pre
            self.tail.next = None
        del current
        
    def __delete_pos(self, pos):
        # Removes element in position passed
        current = self.head
        pre = Node(None)
        for i in range(1, pos):
            pre = current
            if current.next != None:
                current = current.next
        
        # Checks if the position is that of the head then calls the delete for first to 
        # preserve head information
        if current == self.head:
            self.__delete_first()
            return
        # Checks if the position is that of the tail then calls the delete for last to 
        # preserve tail information
        if current == self.tail:
            self.__delete_last
            return
        # If it's a middle position then deletes it
        pre.next = current.next
        del current

    def print_list(self):
        if self.head == None:
            print("Empty List")
        else:
            worker = self.head
            while worker != None:
                print("[" + str(worker.val) + "]", end="", flush = True)
                if worker.next != None:
                    print(" -> ", end="", flush = True)
                else:
                    print("\n")
                worker = worker.next