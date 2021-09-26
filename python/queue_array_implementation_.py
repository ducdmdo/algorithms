
class Queue:
    def __init__(self):
        self.itemList =[]

    def enqueue(self, data):
        self.itemList.insert(0, data)

    def dequeue(self):
        return self.itemList.pop()

    def size(self):
        return len(self.itemList)

    def isEmpty(self):
        return len(self.itemList) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue("doo")
q.enqueue("dog")
q.enqueue(True)
q.enqueue(False)
q.enqueue("dsfasf")
q.dequeue()

print (q.size())