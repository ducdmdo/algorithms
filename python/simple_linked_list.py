class Element:
    data = None
    next_node = None

    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return "returning data: %s" % self.data

class linked_list:

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

    def add(self, value):
        new_node = Element(value)
        new_node.next_node = self.head
        self.head = new_node

ll = linked_list()
ll.add(1)





