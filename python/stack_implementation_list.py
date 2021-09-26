class Stack():

    def __init__(self):
        self.itemList = []

    def __repr__(self):
        listOfItems=[]
        for i in self.itemList:
            listOfItems.append(i)
        return '->'.join(listOfItems)

    def isEmpty(self):
        return len(self.itemList) == 0

    def push(self, item):
        self.itemList.insert(0,item)

    def pop(self):
        return self.itemList.pop(0)


    def peek(self):
        return self.itemList(0)

    def size(self, stackObject=[]):
        return len(stackObject = self.stackOject)



stack = Stack()
stack.isEmpty()
stack.push("hello")
stack.push("true")
stack.push("aloha")
stack.push("123")
stack.push("hello world")
print (stack)
print (stack.pop())
print (stack)


