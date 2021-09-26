class Node:
    def __init__(self, initialData):
        self.data = initialData
        self.nextNode = None

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode

    def setData(self, inputData):
        self.data = inputData

    def setNextNode(self, newNextNode):
        self.nextNode = newNextNode


class Stack:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.getNextNode() is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.getNextNode()
        return '->'.join(nodes)

    def isEmpty(self):
        return self.head == None

    def pop(self):
        currentNode = self.head
        if not self.isEmpty():
            self.head = currentNode.getNextNode()
            currentNode.setNextNode(None)
        else:
            print("The stack is empty, so thera is no thing to pop")

    def push(self, inputData):
        newNode = Node(inputData)
        currentNode = self.head
        if not self.isEmpty():
            newNode.setNextNode(currentNode)
            self.head = newNode
        self.head = newNode


def parChecker(symbolString):
    balanced = True
    s = Stack()
    rounded_number = (len(symbolString)) % 2
    if rounded_number != 0:
        return False
    for sym in symbolString:
        if sym == "(":
            s.push(sym)
        if sym == ")":
            if s.isEmpty():
                return False
            s.pop()
    if s.isEmpty():
        return balanced


print(parChecker('((()))'))
print(parChecker('(()'))
