class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None

class LinkedList:
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

    def insertToLast(self, value):
        newNode = Node(value)
        currentNode = self.head
        if currentNode is None:
            self.head = newNode
        else:
            while currentNode.nextNode:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode

    def reverseLinkedList(self, currentNode):
        if (currentNode.nextNode is None):
            self.head =  currentNode
            return
        self.reverseLinkedList(currentNode.nextNode)
        tmpNode = currentNode.nextNode
        tmpNode.nextNode = currentNode
        currentNode.nextNode = None

# Helper function to print a given linked list
def printList(msg, head):
    print(msg, end='')

    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.nextNode
    print("None")

ll = LinkedList()
ll.insertToLast('H')
ll.insertToLast('E')
ll.insertToLast('L')
ll.insertToLast('L')
ll.insertToLast('O')


printList ("head: ", ll.head)
ll.reverseLinkedList(ll.head)
printList ("head: ", ll.head)
#print (ll)



