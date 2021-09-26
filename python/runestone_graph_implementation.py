class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + ' connectedTo:' + str([x.id for x in self.connectedTo])

    def addNeighbor (self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight (self, neighbor):
        return self.connectedTo[neighbor]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self, fromNode, toNode, weight=0):
        if fromNode not in self.vertList:
            nv = self.addVertex(fromNode)
        if toNode not in self.vertList:
            nv = self.addVertex(toNode)
        self.vertList[fromNode].addNeighbor(self.vertList[toNode], weight)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


    def graph_presentation(self):
        g = Graph()
        for i in range(6):
            g.addVertex(i)
        g.vertList()
        g.addEdge(0,1,5)
        g.addEdge(0, 5, 2)
        g.addEdge(1, 2, 4)
        g.addEdge(2, 3, 9)
        g.addEdge(3, 4, 7)
        g.addEdge(3, 5, 3)
        g.addEdge(4, 0, 1)
        g.addEdge(5, 4, 8)
        g.addEdge(5, 2, 1)

        for v in g:
            for w in v.getConnections():
                print("(%s, %s)" % (v.getId(), w.getId()))



