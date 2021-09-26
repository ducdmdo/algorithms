class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild != None:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        else:
            self.leftChild = BinaryTree(newNode)


    def insertRight(self,newNode):
        if self.rightChild != None:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
        else:
            self.rightChild = BinaryTree(newNode)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
