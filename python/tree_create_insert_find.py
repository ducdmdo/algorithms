# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)

"""
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
"""


"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        nodes = []
        current = self.value
        while current:
            if current is self.value:
                nodes.append("[root: %s]" % current)
            elif current.left is None:
                nodes.append("[left node: %s]" % current.left)
                current = current.left
            else:
                nodes.append("[right node: %s]" % current.right)
                current = current.right
        return '->'.join(nodes)

    def insert(self, element):
        currentNode = self.value
        if currentNode == None:
            return element

        if element <= currentNode:
            while self.left:
                self.left = self.left.left
            self.left = element

        if element > currentNode:
            while self.right:
                self.right = self.right.right
            self.right = element

# helper to create value for node
    def getNewNode(iNode):
        iNode.value = None
        # newNode.value = data
        iNode.left = iNode.right = None
        return iNode

"""

"""


class BinaryTree(object):
    def __init__(self, root):
        self.root = root


bst = Node(1)

print (bst.insert(2))
print (bst)
"""

