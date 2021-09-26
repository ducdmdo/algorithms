class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data=data

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

    def __isempty__(self):
        return self.head == None

    def size(self):
        current=self.head
        count=0
        while current:
            current+=1
            current=current.next_node
        return count

    def add(self,data):
        New_Node = Node(data)
        New_Node.next_node=self.head
        self.head=New_Node

    def search(self,key):
        current = self.head
        while current:
            if current==key:
                return "Found result %s" % current
            else:
                current=current.next_node
        return None

    def getposition(self,position):
        counter=0
        current=self.head

        while current and counter<=position:
            if counter==position:
                return current.data
            current=current.next_node
            counter +=1
        return None

    def insert(self, data, index):
        if index==0:
            self.add(data)

        new = Node(data)
        position = index
        current = self.head
        counter=1

        while position>1 and counter<=position:
            if counter == position:
                new.next_node=current.next_node
                current.next_node=new
            current=current.next_node
            counter +=1

        if position==1:
            new.next_node = current.next_node
            current.next_node = new


    def remove(self,key):
        current = self.head
        previous = None
        found=False

        while current and not found:
            if current.data==key and current is self.head:
                found=True
                self.head = current.next_node
            elif current.data==key:
                found=True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

ll = linked_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
print (ll)
ll.remove(4)











