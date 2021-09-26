
class Vertex: # Vertext object
    def __init__(self, id):
        self.id = id
        self.connectedTo = {} # This is the dictionary. key = Vertex object; value = weight

    def addConnection(self, neightbor, weight =0):
        self.connectedTo[neightbor] = weight

    def getConnection(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def __str__(self):
        return str(self.id) + 'connected to: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.VerList = {} # Graph dictionary. key = Vertext-id, value = Vertex object
        self.size = 0

    def __iter__(self):
        return iter(self.VerList.values())

    def addVertex(self, key):
        self.size = self.size + 1
        if id not in self.VerList:
            self.VerList[key] = Vertex(id)
        return self.VerList

    def addEdge(self, fromVertextKey, toVertextKey, weight=0):
        if fromVertextKey not in self.VerList:
            self.addVertext(fromVertextKey)
        if toVertextKey not in self.VerList:
            self.addVertext(toVertextKey)
        self.VerList[fromVertextKey].addConnection(self.VerList[toVertextKey], weight)

def buildGraph(worldFile):
    dic = {}
    graph = Graph()
    wfile = open(worldFile, 'r')
    #Create buckets of words that differ from one letter
    for line in wfile:
        word = line[:-1]
        for item in range(len(word)):
            bucket = word[:item] + '_' + word[item+1:]
            if bucket in dic:
                dic[bucket].append(word) #append the value to the value list
            else: dic[bucket] = [word]
    #Add vertices and edges for words in the same bucket
    for bucket in dic.keys():
        for word1 in dic[bucket]:
            for word2 in dic[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)
    return graph
