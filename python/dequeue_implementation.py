class Dequeue:
    def __init__(self):
        self.itemList =[]

    def isEmpty(self):
        return len(self.itemList) == 0

    def addFront(self, data):
        self.itemList.append(data)

    def addRear(self, data):
        self.itemList.insert(0,data)

    def removeFront(self):
        return self.itemList.pop()

    def removeRear(self):
        return self.itemList.pop(0)

    def size(self):
        return len(self.itemList)