class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next
        return '->'.join(nodes)

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        currentNode = self.head
        if currentNode is None:
            self.head = temp
            self.tail = temp
        else:
            temp.setNext(self.head)
            self.head = temp
            while currentNode.getNext() is not None:
                currentNode = currentNode.getNext()
            self.tail = currentNode

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        newNode = Node(item)
        currentNode = self.head
        tailNode: UnorderedList = self.tail
        if currentNode is None:
            self.head = newNode
        else:
            tailNode.next = newNode
            self.tail = newNode


mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.append(8)

print(mylist)
