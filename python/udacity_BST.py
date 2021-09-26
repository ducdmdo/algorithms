"""
This time, you'll implement search() and insert().
You should rewrite search() and not use your code from the last exercise so it takes advantage of BST properties.
Feel free to make any helper functions you feel like you need, including the print_tree() function from earlier for debugging.
You can assume that two nodes with the same value won't be inserted into the tree.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        currentRoot = tree.root
        if currentRoot is None:
            return currentRoot
        elif currentRoot:
            if currentRoot.value == new_val:
                return currentRoot
        elif new_val <= currentRoot.value:
            currentRoot.right = self.insert(currentRoot.right, new_val)
        else:
            currentRoot.left = self.insert(currentRoot.left, new_val)


    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))
print (tree.print_tree())