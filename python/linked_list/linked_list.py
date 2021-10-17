import re

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
      while curent :


          if curent.data==data:
              curent= curent.next
              return True

          else:return False
  def append(self, value):
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

  def insert_before(self,value,new_value):
        if self.head is None:
            print("List has no element")
            return

        if value == self.head.data:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        print(current.next)
        while current.next is not None:
            if current.next.data == value:
                break
            current = current.next
        if current.next is None:
            print("item not in the list")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node

  def insert_after(self,value,new_value):
      current = self.start_node
      print(current.next)
      while current is not None:
        if current.data == value:
            break
        current = current.next
      if current is None:
        print("item not in the list")
      else:
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node









# "{  } -> {  } -> {  } -> NULL"

  def to_string(self):
      curent=self.head
      new_list=[]

      while curent:

        #  some_data=f"{ {str(curent.data)}} => "
          some_data=curent.data
          new_list.append( some_data)
          curent=curent.next
      print(len(new_list))
      return new_list
    #   new_list.append("NULL")
    #   list=str(new_list)
    #   x=re.sub(',(?!\s+\d$)', '', list)
    #   y=re.sub("(?!\s+\d$)", "", x)
    #   print(y)


li=LinkedList()
li.append(5)
li.append(0)
li.append(4)
li.insert_before(4,2)
li.includes(9)
print(li.to_string())
