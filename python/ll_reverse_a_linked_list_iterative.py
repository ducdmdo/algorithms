class element:
    def __init__(self, value):
        self.data = value
        self.nextNode = None


class linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.nextNode
        return '->'.join(nodes)

    def addToLastItem(self, value):
        newNode: element = element(value)
        currentNode = self.head

        if self.head is None:
            self.head = newNode
        else:
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode
            newNode.nextNode = None

def reverseLinkedList(inputString):
    ll = linkedlist()
    for ch in inputString:
        ll.addToLastItem(ch)
    print (ll)
    previousNode = None
    currentNode = ll.head
    next_Node = None
    while (currentNode is not None):
        next_Node = currentNode.nextNode
        currentNode.nextNode = previousNode
        previousNode = currentNode
        currentNode = next_Node
    ll.head = previousNode
    print(ll)


print(reverseLinkedList("Hello world 123"))
