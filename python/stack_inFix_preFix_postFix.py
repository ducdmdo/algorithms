import logging

class Stack:
    def __init__(self):
        self.itemList = []

    def push(self, value):
        self.itemList.insert(0,value)

    def pop(self):
        if not self.isEmpty():
            return self.itemList.pop(0)
        return None

    def isEmpty(self):
        return len(self.itemList) == 0

    def size(self):
        return len(self.itemList)

    def peek(self):
        if not self.isEmpty():
            return self.itemList[0]
        return None

def higherDegreeOperand(first_Operand, second_Operand):
    operand = {}
    operand[None] = 0
    operand["+"] = 1
    operand["-"] = 2
    operand["*"] = 3
    operand["/"] = 4
    operand["^"] = 5
    key_list = list(operand.keys())
    higherOperand =  max(operand[first_Operand], operand[second_Operand])
    return key_list[higherOperand]

print (higherDegreeOperand(None,"^"))

def parChecker(symbolString):
    balanced = True
    s = Stack()
    open_symbols = ["(", "[", "{"]
    close_symbols = [")", "]", "}"]
    #rounded_number = (len(symbolString)) % 2
    #if rounded_number != 0:
    #    return False
    for sym in symbolString:
        if sym in open_symbols:
            s.push(sym)
        if sym in close_symbols:
            if s.isEmpty():
                return False
            peek = s.pop()
            if not isMatchedSymbol(peek, sym):
                return False
    if s.isEmpty():
        return balanced

def isMatchedSymbol(open, close):
    open_symbols = ["(", "[", "{"]
    close_symbols = [")", "]", "}"]
    return open_symbols.index(open) == close_symbols.index(close)


def inFixToPostFix(inPut_Arithmetic):

    openParentheses = "("
    closeParentheses = ")"
    operatorList = "0123456789ABCDEFGHIJKLMNOPQRSTVUWXYZ"
    store_Stack = Stack()
    postfixList = []
    operand = {}
    operand[None] = 0
    operand["("] = 1
    operand["+"] = 2
    operand["-"] = 3
    operand["*"] = 4
    operand["/"] = 5
    operand["^"] = 6

    # check if the input Arithmetic is parentheses balanced
    if not parChecker(inPut_Arithmetic):
        return "The input is not balanced symbols"
    # Parse every element in the input Arithmetic
    for element in inPut_Arithmetic:
        # Check if the parsed element is the operator then put it into operator list
        if element in operatorList:
            postfixList.append(element)
        # Check if the parsed element is the open (left) parentheses then push it into the parentheses stack
        elif element == openParentheses:
            store_Stack.push(element)
        # Check if the parsed element is the close (right) parentheses then pop the open (left) parentheses in
        # parentheses stack Fetch the operand from the operand stack
        elif element == closeParentheses:
            topElement = store_Stack.pop()
            while topElement != openParentheses:
                postfixList.append(topElement)
                topElement = store_Stack.pop()
        else:
            while (not store_Stack.isEmpty()) and operand[store_Stack.peek()] > operand[element]:
                postfixList.append(store_Stack.pop())
            store_Stack.push(element)

    while not store_Stack.isEmpty():
        postfixList.append(store_Stack.pop())
    return " ".join(postfixList)


print (inFixToPostFix("A+B*C+D"))
print (inFixToPostFix("(A+B)*C-(D-E)*(F+G)"))

