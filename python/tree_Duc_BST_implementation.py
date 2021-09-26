class Node:
    def __init__(self, rootObj):
        self.data = rootObj
        self.left = None
        self.right = None

    def __repr__(self):
        nodes = []
        nodes.append("[Root: %s]" % self.data)
        if self.left:
            nodes.append("[Left Child %s]" % self.left)
            self.left.__repr__()
        else:
            nodes.append("[Right Child: %s]" % self.right)
            self.right.__repr__()
        return '->'.join(nodes)

    def getRootValue(self):
        return self.data

    def getLeftChildren(self):
        return self.left

    def getRightChild(self):
        return self.right

    def hasAnyChildren(self):
        return self.left or self.right

    def hasRightChildren(self):
        return self.right

    def hasLeftChildren(self):
        return self.left

class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        nodes = []
        nodes.append("[Root: %s]" % self.root.data)
        if self.left:
            nodes.append("[Left Child %s]" % self.left.data)
            self.left.__repr__()
        elif self.right:
            nodes.append("[Right Child: %s]" % self.right.data)
            self.right.__repr__()
        return '->'.join(nodes)

    def insert (self, data):
        newNode = Node(data)
        currentNode = self.root
        if currentNode is None:
            self.root = newNode
        elif currentNode.hasAnyChildren():
            while currentNode.hasAnyChildren():
                if newNode.data < currentNode.data:
                    if currentNode.hasLeftChildren():
                        currentNode = currentNode.left
                    else: currentNode.left = newNode
                elif newNode.data > currentNode.data:
                    if currentNode.hasRightChildren():
                        currentNode = currentNode.right
                    else: currentNode.right = newNode
                elif newNode.data == currentNode.data:
                    print (" The node %s is existing in the tree" % newNode.data)
            if newNode.data < currentNode.data:
                currentNode.left = newNode
            elif newNode.data > currentNode.data:
                currentNode.right = newNode
        else:
            if newNode.data < currentNode.data:
                currentNode.left = newNode
            if newNode.data > currentNode.data:
                currentNode.right = newNode


    def search (self, data):
        currentNode = self.root
        if currentNode.data == data:
            return currentNode
        else:
            while currentNode.hasAnyChildren():
                if data < currentNode.data and currentNode.hasLeftChildren():
                    currentNode = currentNode.left
                    if data == currentNode.data:
                        print ("Found the node %s in the left: " % currentNode.data)
                        return currentNode
                if data > currentNode.data and currentNode.hasRightChildren():
                    currentNode = currentNode.right
                    if data == currentNode.data:
                        print ("Found the node %s in the right: " % currentNode.data)
                        return currentNode
            return None

def minChild(input_min_Child):
    if input_min_Child is None:
        return input_min_Child
    while input_min_Child.left is not None:
        input_min_Child = input_min_Child.left
    print ("min value is: %s" %input_min_Child.data )
    return input_min_Child


def delete_node(root, deleteData):
    currentNode = root
    if currentNode is None:
        return currentNode
    if deleteData < currentNode.data:
        currentNode.left = delete_node(currentNode.left, deleteData)
    elif deleteData > currentNode.data:
        currentNode.right = delete_node(currentNode.right, deleteData)
    # Delete node if the node.data is matching with deleteData
    else:
        # Node with only one child or no child
        if currentNode.left is None:
            temp = currentNode.right
            root = None
            return temp

        elif currentNode.right is None:
            temp = currentNode.left
            root = None
            return temp
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minChild(currentNode.right)

        # Copy the inorder successor's
        # content to this node
        currentNode.key = temp.key

        # Delete the inorder successor
        currentNode.right = delete_node(currentNode.right, temp.key)
    return currentNode






bst = BST()
bst.insert(17)
bst.insert(5)
bst.insert(2)
bst.insert(35)
bst.insert(11)
bst.insert(29)
bst.insert(38)
bst.insert(9)
bst.insert(16)
bst.insert(7)
bst.insert(8)

delete_node(bst, 7)
print (bst.search(17))
print (bst.search(5))
print (bst.search(2))
print (bst.search(35))
print (bst.search(11))
print (bst.search(29))
print (bst.search(38))
print (bst.search(9))
print (bst.search(16))
print (bst.search(7))
print (bst.search(8))




