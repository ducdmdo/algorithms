class Stack:
    def __init__(self):
        self.itemList = []

    def push(self, inputData):
        self.itemList.insert(0,inputData)

    def pop(self):
        return self.itemList.pop(0)

    def isEmpty(self):
        return len(self.itemList) == 0

def convert_Decimal_Binary(inputNumber): # deivde by 2
    outputBinary = ""
    s = Stack()
    while inputNumber >0:
        remainder = inputNumber % 2
        s.push(remainder)
        inputNumber = inputNumber // 2
    while not s.isEmpty():
        outputBinary = outputBinary + str(s.pop())
    return outputBinary

def baseConverter(inputNumber, base):
    digits ='0123456789ABCDEF'

    s = Stack()
    while inputNumber >0:
        remainder = inputNumber % base
        s.push(remainder)
        inputNumber = inputNumber // base
    outputBinary = ""
    while not s.isEmpty():
        outputBinary = outputBinary + digits[s.pop()]
    return outputBinary


print (convert_Decimal_Binary(125))
print (baseConverter(125,16))