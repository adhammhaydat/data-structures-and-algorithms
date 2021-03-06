from linked_list.stack_and_queue import Stack,Queue
# from linked_list.linked_list import Node
from linked_list.pseudo_queue import Pseudo_queue
from linked_list.stack_queue_animal_shelter import Cat,Dog,Animal_shelter
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
    excepted =True
    #Act

    actuale = stack.is_empty()
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

def test_enqueue():
    #range
    queue=Queue()
    queue.enqueue(1)
    excepted=1
    actuale=queue.peek()
    assert actuale==excepted

def test_enqueue_multiple_values_into_queue():
    #range
    excepted=1
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    actuale=queue.peek()
    assert actuale==excepted

def test_dequeue_in_queue(queue):
    #range
    excepted=2
    queue.dequeue()
    actuale=queue.peek()
    assert actuale==excepted

def test_peek_in_queue(queue):
    #range
    excepted=2
    queue.dequeue()
    actuale=queue.peek()
    assert actuale==excepted

def test_empty_queue_after_multiple_dequeues(queue):
    with pytest.raises(Exception):
        #range

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        actuale=queue.is_empty()

def test_instantiate_an_empty_queue():
    excepted=True
    queue=Queue()
    actuale=queue.is_empty()
    assert actuale==excepted

def test_dequeue_on_empty_queue_raises_exception():
    with pytest.raises(Exception):
        queue=Queue()
        queue.dequeue()

def test_enqueue_pseudo():
    #range
    queue=Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    excepted1=1
    excepted2=2
    actuale1=queue.front.data
    actuale2=queue.rear.data
    assert actuale1==excepted1
    assert actuale2==excepted2

def test_dequeue_pseudo():
    queue=Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    excepted =2
    actuale=queue.dequeue()
    assert actuale==excepted

################################# test animal_shetrt ###########################################3#############
def test_enqueue_animal_shelter():
    #range
    cat=Cat()
    dog=Dog()
    animal=Animal_shelter()
    animal.enqueue(cat)
    animal.enqueue(dog)
    excepted1='cat'
    excepted2="dog"
    actuale1=animal.front_cat.type
    actuale2=animal.front_dog.type
    assert actuale1==excepted1
    assert actuale2==excepted2

def test_dequeue_animal_shelter():
    #range
    cat=Cat()
    dog=Dog()
    animal=Animal_shelter()
    animal.enqueue(cat)
    animal.enqueue(dog)
    excepted1='cat'
    excepted2="dog"
    actuale1=animal.dequeue('cat')
    actuale2=animal.dequeue('dog')
    assert actuale1==excepted1
    assert actuale2==excepted2
