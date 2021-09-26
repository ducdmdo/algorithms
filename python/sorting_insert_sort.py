def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


def insertionSorting(itemList):
    index = 1
    while index < len(itemList):
        currentValue = itemList[index]
        position = index

        while position > 0 and itemList[position-1] > currentValue:
            itemList[position] = itemList[position-1]
            position = position - 1

        itemList[position] = currentValue
        index = index + 1

alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
insertionSorting(alist)

print(alist)
#print(insertionSorting)
