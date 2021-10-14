

from typing import Counter


class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

class LinkedList:

  """
  A class for creating instances of a Linked List.

  Data and other attributes defined here:

  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """

    # create new node

    # self.head =new_node
    current = self.head
    if current == None:
        self.head = Node(value, self.head)
        return
    while current.next != None:
            current=current.next
    new_node=Node(value)

    current.next=new_node



  def includes(self,data):
      """"
       include method for iterat over a linkedlist to check if the
       value are exist or not

      arguments:
      value : any

      returns: boolian
      """
      curent=self.head
      if not self.head:
          return False
      while curent :


          if curent.data==data:
              curent= curent.next
              return True

          else:return False






  def to_string(self):
      curent=self.head
      while curent.next :

          return curent.data


li=LinkedList()
li.insert(5)
li.insert(0)
li.includes(9)
li.to_string()
