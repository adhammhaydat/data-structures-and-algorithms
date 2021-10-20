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


    self.head = Node(value, self.head)



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
    if not current :
        self.head = Node(value, self.head)
        return
    while current.next :
            current=current.next
    new_node=Node(value)

    current.next=new_node


  def insert_before(self,value,new_value):
        if self.head is None:
            print("List has no element")
            return "List has no element"

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
      current = self.head
      print(current.next)
      while current is not None:
        if current.data == value:
            break
        current = current.next
      if current is None:
        return "item not in the list"
      else:
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node

  def kth_from_end(self,target):
        current = self.head
        count=0
        while current:
            count += 1
            current = current.next
        current=self.head
        if target < count >=0:

            for i in range(1,count-target-1):
                current = current.next
            return current.data
        elif target>count-1:
            raise Exception('the target greater than count of element in the linked list')
        elif target < 0:
            raise Exception('value not positive')
  def revers(self):
      prev=None
      current=self.head
      while  current is not None:
        next=current.next
        current.next=prev
        prev = current
        current = next
      self.head=prev
  def __str__(self):
      curent=self.head
      new_string=''
      while curent:
          new_string +=f"{{{curent.data}}} -> "
          curent=curent.next
      new_string +="NULL"
      return new_string

def zip_lists(linked_a, linked_b):
    current1=linked_a.head
    current2=linked_b.head
    helper=''
    if not current1 and not current2:
        return 'empty list'
    if not current1:
        return str(linked_b)
    if not current2:
        return str(linked_a)
    while current1 and current2:
        if current2:
            helper=current1.next
            current1.next=current2
            current1=helper
        if current1:
            helper=current2.next
            current2.next=current1
            current2=helper
    return str(linked_a)
li=LinkedList()
l2=LinkedList()
l3=LinkedList()
li.insert(5)
li.append(0)
li.append(4)
# li.insert_before(4,2)
# li.includes(9)
# li.kth_from_end(3)
print(li)

l2.insert(1)
l2.append(2)
l2.append(3)
l3.insert(1)
l3.append(2)
l3.append(3)
l3.revers()
print(l3)
print(zip_lists(li,l2))


