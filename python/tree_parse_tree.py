import operator

class Stack():

    def __init__(self):
        self.itemList = []

    def __repr__(self):
        listOfItems=[]
        for i in self.itemList:
            listOfItems.append(i)
        return '->'.join(listOfItems)

    def isEmpty(self):
        return len(self.itemList) == 0

    def push(self, item):
        self.itemList.insert(0,item)

    def pop(self):
        return self.itemList.pop(0)


    def peek(self):
        return self.itemList(0)

    def size(self, stackObject=[]):
        return len(stackObject = self.stackOject)

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


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
evaluate(pt)
print (evaluate(pt))
#pt.postorder()  #defined and explained in the next section
