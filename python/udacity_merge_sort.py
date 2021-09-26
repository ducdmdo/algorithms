def merge_sort(list):
    """
    Sorts a list in an acceding order

    Divide: Find a midpoint of the list and divide into the sublist
    Conquer: Recursively sort the sublists created in the previous steps
    Combine: Merge the sorted sublist created in the previous steps
    :param list: list of items
    :return: a new sorted list
    """
    if len(list)<=1:
        return(list)

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left,right)
def split(list):
    """
    Divide the unsorted list at the midpoint into sublist
    Return 2 sublists: left and right
    :param list:
    :return:
    """
    midpoint=len(list)//2
    left=list[:midpoint]
    right =list[midpoint:]
    return left, right


def merge(left,right):
    """
    Merge 2 lists and sort them in process
    Return a new sorted list
    :param left:
    :param right:
    :return:
    """
    l=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
    while i<len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[j])
        j+=1
    return l

def verify_sorted_list(list):
    n=len(list)
    if n==0 and n==1:
        return True
    return list[0] < list[1] and verify_sorted_list(list[1:])

alist=[23,5,35,67,37,743,12,7,7,23,7,85,89]

verify_sorted_list(alist)
print (alist)
verify_sorted_list(merge_sort(alist))

