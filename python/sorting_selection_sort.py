def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


def selection_Sorting(itemList):
    index = 0
    currentItemLength = len(itemList)

    while index < (len(itemList)-1):
        maxPosition = 0
        for position in range(1, currentItemLength):
            if itemList[position] > itemList[maxPosition]:
                maxPosition = position

        # move the biggest items to the last item
        temp = itemList[position]
        itemList[position] = itemList[maxPosition]
        itemList[maxPosition] = temp

        # Adjust the latest item position
        currentItemLength = currentItemLength - 1

        #proceed for the next big item
        index = index + 1

alist = [54,26,93,17,77,31,44,55,20]
#selectionSort(alist)
selection_Sorting(alist)
print(alist)
print(alist)

