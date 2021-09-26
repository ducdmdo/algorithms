class Vertex:  # Vertex object
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}  # This is the dictionary containing pair of key (Vertex object), value (weight)

    def addConnection(self, neightbor, weight):
        self.connectedTo[neightbor] = weight


class Graph:  # Graph object
    def __init__(self):
        self.size = 0
        self.verList = {}  # This is the dictionary containing pair of key (Vertex id); value (Vertex object)

    def addVertex(self, key):
        if key not in self.verList:
            self.verList[key] = Vertex(key)
            self.size = self.size + 1

    def addEdge(self, fromVerID, toVerID, weight):
        if fromVerID not in self.verList:
            self.verList[fromVerID] = Vertex(fromVerID)
        if toVerID not in self.verList:
            self.verList[toVerID] = Vertex(toVerID)
        self.verList[fromVerID].addConnection(self.verList[toVerID], weight)


def knightGraph(bdSize):
    kGraph = Graph()
    for row in range(bdSize):
        for column in range(bdSize):
            nodeID = positionToNodeID(row, column, bdSize)
            newPositions = generateLegalMove(row, column, bdSize)
            for edge in newPositions:
                nID = positionToNodeID(edge[0], edge[1], bdSize)
                kGraph.addEdge(nodeID, nID, 0)
    return kGraph


def positionToNodeID(row, col, board_size):
    return (row * board_size) + col


def generateLegalMove(row, col, board_size):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newRow = row + i[0]
        newCol = col + i[1]
        if legalCoord(newRow, board_size) and legalCoord(newCol, board_size):
            newMoves.append((newRow, newCol))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

knightGraph(4)
