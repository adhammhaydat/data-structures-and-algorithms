# Stacks and Queues
<!-- Short summary or background information -->
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge
<!-- Description of the challenge -->
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

pull req: https://github.com/adhammhaydat/data-structures-and-algorithms/pull/31

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
in the first create class node and then create other classes dependent on class node
followed the approach to sure the the big o be lowest

## API
<!-- Description of each method publicly available to your Stack and Queue-->
1. class Stack: contain 4 method
    - push: adds a new node with that value to the top of the stack with an O(1) Time performance.
    - pop: Removes the node from the top of the stack
    - peek: Returns value of the node located at the top of the stack
    - is_empty: Returns boolean indicating whether or not the stack is empty.
2. class Queue: contain 4 method
    - enqueue: adds a new node with that value to the rear of the queue with an O(1) Time performance.
    - dequeue: Removes the node from the front of the queue
    - peek: Returns value of the node located at the front of the queue
    - is_empty: Returns boolean indicating whether or not the queue is empty
