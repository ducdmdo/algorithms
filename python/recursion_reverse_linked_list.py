class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next


# Helper function to print a given linked list
def printList(msg, head):
    print(msg, end='')

    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")

def reverseList_anotheVersion(self, head):
    if not head or not head.next:
        return head
    second = head.next
    reverse = self.reverseList(second)
    second.next = head
    head.next = None
    return reverse

def reverseList(head):
    """
    :type head: ListNode
    :rtype: Node
    """
    if head is None:
        return head
    if head.next is None:
        return head
    rl = reverseList(head.next)
    head.next.next = head
    head.next = None
    #head = rl
    #printList("head: ", head)
    printList("rl: ", rl)
    return rl




head = None
head = Node(4, head)
head = Node(3, head)
head = Node(2, head)
head = Node(1, head)

printList("Before: ", head)
reverseList(head)
printList("After: ", reverseList(head))