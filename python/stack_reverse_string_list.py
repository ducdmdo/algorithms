from stack_implementation_list import Stack


def reverseString(inputString):
    stack = Stack()
    outputResult = ''
    for i in inputString:
        stack.push(i)
    while not stack.isEmpty():
        outputResult = outputResult + stack.pop()
    return outputResult


print (reverseString('Hello world 123 !!!'))

