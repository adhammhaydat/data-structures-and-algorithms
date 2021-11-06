from python.linked_list.tree_fizz_buzz import Node,fizz_buzz,Binary_search_tree

def  test_fizz_buzz():
    tree = Binary_search_tree()
    a_node = Node(3)
    b_node = Node(6)
    c_node = Node(9)
    d_node = Node(4)
    e_node = Node(5)
    f_node = Node(15)


    a_node.child.append(b_node)
    a_node.child.append(d_node)
    b_node.child.append(c_node)
    c_node.child.append(e_node)
    a_node.child.append(f_node)
    tree.root = a_node
    expected=['Fizz', 'Fizz', '4', 'FizzBuzz', 'Fizz', 'Buzz']
    actul=fizz_buzz(tree).bfs()
    assert actul==expected
    
test_fizz_buzz()
