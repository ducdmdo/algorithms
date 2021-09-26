class Element:
    def __init__(self, value):
        self.data = value
        self.nextNode = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addToLast(self, value):
        newNode = Element(value)
        currentNode = self.head
        if currentNode is None:
            self.head = newNode
        else:
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode

    def printForward(self, currentNode):
        if currentNode is None:
            return
        print ('%s ' % currentNode.data)
        self.printForward(currentNode.nextNode)

    def printReverse(self, currentNode):
        if currentNode is None:
            return
        self.printReverse(currentNode.nextNode)
        print ('%s ' % currentNode.data)


ll = Linkedlist()
ll.addToLast('H')
ll.addToLast('e')
ll.addToLast('l')
ll.addToLast('l')
ll.addToLast('o')

ll.printForward (ll.head)
ll.printReverse(ll.head)




