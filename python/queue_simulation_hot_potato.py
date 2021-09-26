class Queue:
    def __init__(self):
        self.itemList = []

    def size(self):
        return len(self.itemList)

    def isEmpty(self):
        return len(self.itemList) == 0

    def enqueue(self, data):
        self.itemList.insert(0, data)

    def dequeue(self):
        return self.itemList.pop()

def hotPotato(nameList, num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)

    while queue.size() > 1:
        for time in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],39))

