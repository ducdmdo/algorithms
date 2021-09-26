class PriorityQueue:
    def __init__(self):
        self.heapList =[0]
        self.currentSize = 0

    def isEmpty(self):
        return len(self.list)

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo ={}

    def addConnection(self, neightbor, weight):
        self.connectedTo[neightbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def delMin(self):
        return self.itemlist.pop() #todo

class Graph:
    def __init__(self):
        self.size = 0
        self.verList = {}
        self.distance = None
        self.Pre = None


    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setPre(self, Pre):
        self.Pre = Pre

    def getPre(self):
        return self.Pre

def dijkstra(aGraph, start):
    priority_queue = PriorityQueue()
    start.setDistance(0)
    priority_queue.buildHeap([(v.getDistance(),v)] for v in aGraph) #todo with buildHeap
    while not priority_queue.isEmpty():
        currentVer = priority_queue.delMin() #todo with delMin
        for nextVer in currentVer.getConnections():
            newDist = currentVer.getDistance() + currentVer.getWeight(nextVer) #todo with getWeight
            if newDist < nextVer.getDistance():
                nextVer.setDistance(newDist)
                nextVer.setPre(currentVer)
                priority_queue.decreaseKey(nextVer, newDist) #todo with

