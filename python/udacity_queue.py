"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""
class Node:
    data = None
    next_node = None

    def __init__(self, value):
        self.data = value

class Queue:
    def __init__(self, head=None):
        self.head = Node(head)

    def __repr__(self):
        queue =[]
        current = self.head
        while current:
            if current is self.head:
                queue.append("[End in line: %s]" % current.data)
            elif current.next_node is None:
                queue.append("[First in line : %s]" % current.data)
            else:
                queue.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(queue)

    def enqueue(self, value):
        new_element = Node(value)
        if self.head == None:
            self.head = new_element
            return self.head
        new_element.next_node = self.head
        self.head = new_element


    def dequeue(self):
        if self.head == None:
            return None
        current_node = self.head
        previous_temp_node = None
        while current_node.next_node:
            previous_temp_node = current_node
            current_node = current_node.next_node
        previous_temp_node.next_node = current_node.next_node

        return previous_temp_node

    #def peek(self):





# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
#print q.peek()

# Test dequeue
# Should be 1
q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
q.dequeue()
# Should be 3
q.dequeue()
# Should be 4
q.dequeue()
q.enqueue(5)
# Should be 5
#print q.peek()