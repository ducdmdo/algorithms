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

def palindromeChecker(inputString):
    dqueue = Dequeue()
    stillEqual = True

    for char in inputString:
        dqueue.addRear(char)

    while dqueue.size()>1 and stillEqual:
        rearItem = dqueue.removeRear()
        frontItem = dqueue.removeFront()
        if rearItem != frontItem:
            stillEqual = False
    return stillEqual

print (palindromeChecker("radar"))
print (palindromeChecker("toot"))
print (palindromeChecker("madam"))
print (palindromeChecker("madamdafagfagag"))