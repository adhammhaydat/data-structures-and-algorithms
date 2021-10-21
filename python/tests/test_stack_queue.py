from linked_list.stack_and_queue import Stack,Queue
from linked_list.linked_list import Node
import pytest

def test_push_onto_stack(stack):
    #range
    excepted="adham"
    #Act
    actuale=stack.peek()
    #assert
    assert actuale==excepted

def test_push_multy_value_stack(stack):
    #range
    excepted="adham"
    #Act
    actuale=stack.peek()
    #assert
    assert actuale==excepted

def test_pop_stack(stack):
    with pytest.raises(Exception):
    #range

    #Act
        stack.pop()
        stack.pop()
        stack.pop()
        actuale=stack.peek()

def test_peek_second_value_stack(stack):
    #range
    excepted = 2
    #Act
    stack.pop()
    actuale = stack.peek()
    #assert
    assert actuale==excepted

def test_instantiate_empty_stack():
    #range
    stack=Stack()
    excepted = None
    #Act

    actuale = stack.value
    #assert
    assert actuale==excepted

def test_peek_empty_stack():
        with pytest.raises(Exception):
            #range
            stack=Stack()
            #Act

            actuale = stack.peek()

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("adham")

    return stack

#################################### **Queue**#####################################
@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("adham")

    return queue

def test_enqueue(queue):
    #range
    excepted=1
    actuale=queue.peek()
    assert actuale==excepted

# def test_enqueue(queue):
#     #range
#     excepted=1
#     actuale=queue.peek()
#     assert actuale==excepted
