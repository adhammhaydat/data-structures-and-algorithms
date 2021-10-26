from linked_list.linked_list import Node
class Stack:

    def __init__(self):
        self.top = None
        self.len = 0


    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.len+=1

    def pop(self):
        if not self.top:
            raise Exception ( 'empty stack')

        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.data

    def __len__(self):
        return self.len


def validate_brackets(string):

    open = ["[","{","("]
    close= ["]","}",")"]
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()
    stack4 = Stack()
    stack5 = Stack()
    stack6 = Stack()
    for value in string:
        if value in open:
            if value == '(':
               stack1.push(value)
            elif value == '[':
                stack2.push(value)
            else:
                stack3.push(value)
        elif value in close:
            if value == ')':
               stack4.push(value)
            elif value == ']':
                stack5.push(value)
            else:
                stack6.push(value)

    if len(stack1) == len(stack4) and len(stack2) == len(stack5) and len(stack3)==len(stack6):
        return True
    else:
        return False



if __name__ == '__main__':
    print('good')
    print(validate_brackets('()[[Extra Characters]]'))
