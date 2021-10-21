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
    #assert

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("adham")

    return stack
