from linked_list.linked_list import Node

class Stack:
    def __init__(self):
        self.top=None
        self.value=None

    def push(self,value):
        """
        Arguments: value
        adds a new node with that value to the top of the stack
        with an O(1) Time performance.
        """
        node=Node(value)
        node.next=self.top
        self.top=node
    def pop(self):
        """
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        """
        if not self.top:
            raise Exception("The stack are empty")
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.data

    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        """
        if not self.top:
            raise Exception("The stack are empty")
        return self.top.data

    def is_empty(slef):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.

        """
        if not Self.top:
            return True
        return False

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        Arguments: value
        adds a new node with that value to the back
        of the queue with an O(1) Time performance.
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
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if not self.rear:
            raise Exception('The queue are empty')
        temp=self.front
        self.front=self.front.next
        temp.next=None
        return self.front.value


    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack

        """
        if not self.front:
            raise Exception("The queue are empty")
        return self.front.data

    def is_empty(self):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        """
        if not self.front:
            return False
        return True
