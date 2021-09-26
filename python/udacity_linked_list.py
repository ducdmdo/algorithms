"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next_node:
                current = current.next_node
            current.next_node = new_element
        else:
            self.head = new_element

    def __repr__(self):
        nodes =[]
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.value)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.value)
            else:
                nodes.append("[%s]" % current.value)
            current = current.next_node
        return '->'.join(nodes)

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1
        if position < 1:
            return None
        while current and count<=position:
            if count==position:
                return current
            current = current.next_node
            count +=1
        return None

    def add(self, data):
        New_Node = Element(data)
        New_Node.next_node = self.head
        self.head = New_Node

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next_node = current.next_node
                    current.next_node = new_element
                current = current.next_node
                counter += 1
        elif position == 1:
            new_element.next_node = self.head
            self.head = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None

        while current.value!=value and current.next_node:
            previous=current
            current=current.next_node
        if current.value==value:
            if previous:
                previous.next_node = current.next_node
            else:
                self.head=current.next_node

"""
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next_node.next_node.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
"""


