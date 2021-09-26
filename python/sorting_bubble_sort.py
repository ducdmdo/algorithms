def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1


def bubbleSort(itemList):
    index = 0
    currentItemLength  = len(itemList)
    exchange = False
    while index < len(itemList) - 1:
        for position in range (0, currentItemLength - 1):
            if itemList[position] > itemList[position+1]:
                exchange = True
                temp = itemList[position+1]
                itemList[position+1] = itemList[position]
                itemList[position] = temp

        currentItemLength = currentItemLength - 1
        index = index + 1

alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSort(alist)
print(alist)