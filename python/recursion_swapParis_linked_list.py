# Definition for singly-linked list.
class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class Solution:

    def addNode(self,node):
        currentNode = self.head
        if currentNode is None:
            self.head = Node(node)
        else:
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = Node(node)

# Helper function to print a given linked list
def printList(msg, head):
    print(msg, end='')

    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")

def swapPairs(head, prev=None):
    # base case: if the list is empty or contains just one node
    if head is None or head.next is None:
        return head

    currentNode = head
    temp = currentNode.next

    currentNode.next = temp.next
    temp.next = currentNode

    if prev is None:
        head = temp
    else:
        prev.next = temp

    prev = currentNode
    swapPairs(currentNode.next, prev)

    return head

head = None
head = Node(4, head)
head = Node(3, head)
head = Node(2, head)
head = Node(1, head)

printList("head: ", head)
head = swapPairs(head, None)
printList("After: ", head)

# The wrapper function to call `rearrange()`
# def rearrangeList(head):
#     return swapPairs(head, None)
#
# if __name__ == '__main__':
#
# 	head = None
# 	for i in reversed(range(8)):
# 		head = Node(i + 1, head)
#
# 	printList("Before: ", head)
# 	head = rearrangeList(head)
# 	printList("After : ", head)






