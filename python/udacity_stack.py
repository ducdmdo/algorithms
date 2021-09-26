"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        #current_head = self.head

        if self.head:
            new_element.next_node = self.head
            self.head = new_element
        else:
            self.head = new_element


    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        Deleted_Node=self.head

        if self.head:
            Deleted_Node.next_node = None
            return Deleted_Node
        else:
            return None



class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def __repr__(self):
        stack =[]
        current = self.ll.head
        while current:
            if current is self.ll.head:
                stack.append("[Top: %s]" % current.value)
            elif current.next_node is None:
                stack.append("[Bottom: %s]" % current.value)
            else:
                stack.append("[%s]" % current.value)
            current = current.next_node
        return '->'.join(stack)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
stack.push(e4)
print (stack.pop())



