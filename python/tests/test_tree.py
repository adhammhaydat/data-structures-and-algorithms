"""
Tests for Binary Tree
"""

from abc import ABC
from linked_list.tree import BinaryTree, Node,breadth_first


def test_bfs():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node("A")
    b_node = Node("B")
    c_node = Node("C")
    d_node = Node("D")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs passed")


def test_bfs_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs_2 passed")


def test_pre_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "4", "3"]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_pre_order_ passed")


def test_post_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "3", "1"]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected


def test_in_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "1", "3"]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_in_order_ passed")


def test_instantiate_an_tree_root():
    excepted = [1]
    tree = BinaryTree()
    tree.root = Node(1)
    actual = tree.in_order()
    assert actual == excepted


def test_instantiate_an_empty_tree():
    excepted = None
    tree = BinaryTree()
    tree.root = None
    actual = tree.in_order()
    assert actual == excepted


def test_max_number():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes
    a_node = Node(1)
    b_node = Node(212)
    c_node = Node(5)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = 212
    # set actual to return value of post_order call
    actual = tree.find_maximum_value()
    # assert actual is same as expected
    assert actual == expected


def test_max_number_with_empty():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    tree.root = None
    # set expected list
    expected = "the tree are empty"
    # set actual to return value of find_maximum_value call
    actual = tree.find_maximum_value()
    # assert actual is same as expected
    assert actual == expected
def test_breadth_first():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(5)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = [1,2,5,4]
    # set actual to return value of post_order call
    actual = breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

def test_breadth_first_empty_tree():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    tree.root=None


    # set expected list
    expected = None
    # set actual to return value of post_order call
    actual = breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected
