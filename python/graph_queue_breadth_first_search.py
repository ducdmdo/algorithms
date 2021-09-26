class Queue:
    def __init__(self):
        self.itemList = []

    def enqueue(self, data):
        self.itemList.insert(0, data)

    def dequeue(self):
        self.itemList.pop()

    def isEmpty(self):
        return len(self.itemList) == 0

    def size(self):
        return len(self.itemList)


class Vertex:  # Vertex object: id is the Vertex id; connectedTo is a dictionary containing a pair of keys (Vertex object) and Values (weight)
    def __init__(self, id, color='White'):
        self.id = id
        self.connectedTo = {}
        self.color = color
        self.distance = None
        self.predecessor = None

    def setDistance(self, weight):
        self.distance = weight

    def getDistance(self):
        return self.distance

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPredecessor(self, VertexObject):
        self.predecessor = VertexObject

    def getPredecessor(self):
        return self.predecessor

    def addConnection(self, neightbor, weight):
        self.connectedTo[neightbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()


class Graph:  # Graph object: size is the Graph's size; VerList contains pair of key (Vertex id) and values (corresponding Vertex object)
    def __init__(self):
        self.size = 0
        self.VerList = {}

    def addVertex(self, key):
        if key not in self.VerList:
            color = 'White'
            self.VerList[key] = Vertex(key, color)

    def addEdge(self, fromVerTexID, toVertexID, weight):
        if fromVerTexID not in self.VerList:
            self.VerList[fromVerTexID] = Vertex(fromVerTexID, 'White')
        if toVertexID not in self.VerList:
            self.VerList[toVertexID] = Vertex(toVertexID, 'White')
        self.VerList[fromVerTexID].addConnection(self.VerList[toVertexID], weight)


def graph_bfs(graphObject, startVertex):
    startVertex.setDistance(0)
    startVertex.setPredecessor(None)
    verQueue = Queue()
    verQueue.enqueue(startVertex)
    while (verQueue.size() > 0):
        currentVer = verQueue.dequeue()
        for nbr in currentVer.getConnections():
            if (nbr.getColor() == 'White'):
                nbr.setColor('Gray')
                nbr.setDistance(currentVer.getDistance() + 1)
                nbr.setPredecessor(currentVer)
                verQueue.enqueue(nbr)
        currentVer.setColor('Black')

# The shortest path is the path that at any Vertex goes back to its predecessor
def shortestPath(startVertex):
    x = startVertex
    while x.getPredecessor():
        print (x.getID())
        x = x.getPredecessor()
    print (x.getID())



