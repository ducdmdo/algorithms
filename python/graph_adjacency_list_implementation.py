class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeightbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + 'connected to: ' + str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else: return None

    def __contains__(self, item):
        return item in self.vertList

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeightbor(self.vertList[t], weight)

def test():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print (g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for vertex_ in g:
        for conectedToVertex in vertex_.getConnection():
            print ("(%s, %s)" % (vertex_.getID(), conectedToVertex.getID()))

test()

