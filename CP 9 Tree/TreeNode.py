class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


    """
    Print a tree visual.

        _ 2 _
       /      \
      7         9
     /  \        \
    1    6         8
        / \       /  \
       5   10    3    4

    """


def pre_order( node):

    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def post_oder( node):

    if node.left:
        post_oder(node.left)
    if node.right:
        post_oder(node.right) 

    print(node)
