class Node:
    
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)
    

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node    
        if node is not None:
            node.parent = self

class BinarySearchTree:

    def __init__(self, node=None):
        self.root = node
    
    def insertion(self, data):
        
        node = Node(data)
        last_node = None
        current_node = self.root

        while current_node is not None:
            last_node = current_node

            if node.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if last_node is None:
            self.root = node
        elif node.data < last_node.data:
            last_node.add_left(node)
        else:
            last_node.add_right(node)

    def pre_order(self, node = None):

        if node == None:
            node = self.root
        print(node)

        if node.left:
            self.pre_order(node.left)

        if node.right:
            self.pre_order(node.right)    
        
