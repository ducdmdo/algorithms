class nodeObject(object):

    def __init__(self, value):
        self.data = value
        self.next_node = None

    def __repr__(self):
        return "returning data: %s" % self.data

class Stack(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes =[]
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)

    def push(self, value):
        newNode = nodeObject(value)
        newNode.next_node = self.head
        self.head = newNode

    def pop(self):
        oldHead = self.head
        self.head = oldHead.next_node
        oldHead.next_node = None

    def isEmpty(self):
        return self.head == None

    def peek(self):
        return self.head

def reverseString(inputString):
    stack = Stack()

    for ch in inputString:
        stack.push(ch)
    print (stack)
    temp = stack.peek()
    stack.head = temp
    stack.pop()
    while (not stack.isEmpty()):
        temp.nextNode = stack.peek()
        stack.pop()
        temp = temp.nextNode
    temp.nextNode = None

print (reverseString("Hello world, aloha 123"))





