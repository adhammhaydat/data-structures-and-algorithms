from linked_list.linked_list import Node
from linked_list.stack_and_queue import Stack

class Pseudo_queue:
    def __init__(self):
        self.front:None
        self.rear=None
        self.stack1:Stack()
        self.stack2:Stack()
    def enqueue(self,value):
        """
        Arguments: value
        Inserts value into the PseudoQueue,
        using a first-in, first-out approach.
        """
        node=Node(value)
        if not self.rear:
            self.rear=node
            self.front=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        """
        Arguments: none
        Extracts a value from the PseudoQueue,
        using a first-in, first-out approach.h
        """
        if not self.front:
            raise Exception('The queue are empty')
        temp=self.front
        self.front=self.front.next
        temp.next=None
        return self.front.data

