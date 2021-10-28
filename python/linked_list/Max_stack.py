
from linked_list import Node

class Max_Stack:
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

    def get_max(self):
        checker=0
        current = self.top
        while current.next:
            if current.data > checker:
                checker=current.data
            current=current.next
        return checker
    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        """
        if not self.top:
            raise Exception("The stack are empty")
        return self.top.data

ll= Max_Stack()
ll.push(1)
ll.push(3)
ll.push(2)
ll.push(4)
ll.push(0)
print(ll.get_max())



