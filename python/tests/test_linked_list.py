from linked_list.linked_list import Node,LinkedList



import pytest

def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
  with pytest.raises(TypeError):
    node = Node()


def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()

  # Act
  ll.insert(1)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected

def test_linked_list_insert_twice():
  # Arrange
    expected = 0
    ll = LinkedList()
    # Act
    ll.insert(0)
    ll.insert(1)
    node = ll.head
    actual = node.data
    # Assert
    assert actual == expected
    assert ll.head.next.data == 1

# Will return true when finding a value within the linked list that exists

def test_linked_list_includes_twice():
  # Arrange
  expected =True
  ll = LinkedList()

  # Act
  ll.insert(0)

  actual = ll.includes(0)

  # Assert
  assert actual == expected


def test_linked_list_includes_twice2():
  # Arrange
  expected =False
  ll = LinkedList()

  # Act
  ll.insert(0)

  actual = ll.includes(1)

  # Assert
  assert actual == expected



# Can properly return a collection of all the values that exist in the linked list
def test_linked_list_to_string_twice():
  # Arrange
  expected =[1,2,3]
  ll = LinkedList()

  # Act
  ll.append(1)
  ll.append(2)
  ll.append(3)
  actual=[]
  actual.append(ll.to_string())

  # Assert
  for i in range(len(actual)):
      assert actual[i] == expected

# def test_linked_list_insert_before_one():
#   expected = [1,2,4,3]
#   ll = LinkedList()

#   # Act
#   ll.append(1)
#   ll.append(2)
#   ll.append(3)
#   ll.insert_before(3,4)
#   actual=[]
#   actual.append(ll.to_string())

#   # Assert
#   for i in range(len(actual)):
#       assert actual[i] == expected

# def test_linked_list_insert_after_one():
#   expected =[1,2,4,3]
#   ll = LinkedList()

#   # Act
#   ll.append(1)
#   ll.append(2)
#   ll.append(3)
#   ll.insert_before(3,4)
#   actual=[]
#   actual.append(ll.to_string())

#   # Assert
#   for i in range(len(actual)):
#       assert actual[i] == expected
