class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percolate_Up(self, iChild):
        while iChild // 2 > 0:
          if self.heapList[iChild] < self.heapList[iChild // 2]:
             tmp = self.heapList[iChild // 2]
             self.heapList[iChild // 2] = self.heapList[iChild]
             self.heapList[iChild] = tmp
          iChild = iChild // 2

    def insert(self, newItem):
      self.heapList.append(newItem)
      self.currentSize = self.currentSize + 1
      self.percolate_Up(self.currentSize)

    def percolate_Down(self, iParent):
      while (iParent * 2) <= self.currentSize:
          mc = self.minChild(iParent)
          if self.heapList[iParent] > self.heapList[mc]:
              tmp = self.heapList[iParent]
              self.heapList[iParent] = self.heapList[mc]
              self.heapList[mc] = tmp
          iParent = mc

    def minChild(self,iParent):
      if iParent * 2 + 1 > self.currentSize:
          return iParent * 2
      else:
          if self.heapList[iParent*2] < self.heapList[iParent*2+1]:
              return iParent * 2
          else:
              return iParent * 2 + 1

    def delete_Min(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percolate_Down(1)
      return retval

    def buildHeap(self,alist):
      item = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (item > 0):
          self.percolate_Down(item)
          item = item - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print (bh)
print(bh.delete_Min())
print(bh.delete_Min())
print(bh.delete_Min())
print(bh.delete_Min())
print(bh.delete_Min())
