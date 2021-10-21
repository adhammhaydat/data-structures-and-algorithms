from linked_list.stack_and_queue import Stack,Queue
from linked_list.linked_list import Node
import pytest

def test_push_onto_stack():
    #range
    excepted="adham"
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("adham")
    #Act
    actuale=stack.peek()
    assert actuale==excepted
