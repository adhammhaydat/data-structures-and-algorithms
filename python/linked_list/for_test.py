class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class BinaryTree:
    def __init_(self):
        self.root = None









def checker(tree1 , tree2):
    breadth = Queue()
    def bfs(tree):
        check = 0
        breadth.enqueue(tree.root)
        while breadth.peek():
            tree.front = breadth.dequeue()

            if not tree.front.left and not tree.front.right:
                check += 1

            if tree.front.left:
                breadth.enqueue(tree.front.left)

            if tree.front.right:
                breadth.enqueue(tree.front.right)

        return check


    couner_tree1 = bfs(tree1)
    couner_tree2 = bfs(tree2)
    print( True) if couner_tree1 == couner_tree2 else print(False)



tree1 = BinaryTree()
tree2 = BinaryTree()

# Create Nodes
a_node = Node(1)
b_node = Node(2)
c_node = Node(5)
d_node = Node(4)
a_node.left = b_node
a_node.right = c_node
b_node.left = d_node

# Add Root node to tree
tree1.root = a_node

# Create Nodes
a_n = Node(1)
b_n= Node(2)
c_n = Node(5)
d_n = Node(4)
a_n.left = b_n
a_n.right = c_n
b_n.left = d_n

# Add Root n to tree
tree2.root = a_n
checker(tree1,tree2)
