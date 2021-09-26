class Node(object):
    def __init__(self, value):
        self.value = value
        self.connectedTo = []

class Edge(object):
    def __init__(self, weight, fromNode, toNode):
        self.weight = weight
        self.fromNode = fromNode
        self.toNode = toNode

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodesList = nodes
        self.edgesList = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodesList.append(new_node)

    def insert_edge(self, new_weight, fromNodeValue, toNodeValue):
        from_found = None
        to_found = None
        for node in self.nodesList:
            if fromNodeValue == node.value:
                from_found = node
            if toNodeValue == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(fromNodeValue)
            self.nodesList.append(from_found)
        if to_found == None:
            to_found = Node(toNodeValue)
            self.nodesList.append(to_found)
        new_edge = Edge(new_weight, from_found, to_found)
        from_found.connectedTo.append(new_edge)
        to_found.connectedTo.append(new_edge)
        self.edgesList.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for edge_object in self.edgesList:
            edge = (edge_object.weight, edge_object.fromNode.value, edge_object.toNode.value)
            edge_list.append(edge)
        return edge_list

    def get_adjacency_list(self):
        max_index = self.find_max_index()
        adjacency_list = [None] * (max_index + 1)
        for edge_object in self.edgesList:
            if adjacency_list[edge_object.fromNode.value]:
                adjacency_list[edge_object.fromNode.value].append((edge_object.toNode.value, edge_object.weight))
            else:
                adjacency_list[edge_object.fromNode.value] = [(edge_object.toNode.value, edge_object.weight)]
        return adjacency_list

    def get_adjacency_matrix(self):
        max_index = self.find_max_index()
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for edge_object in self.edgesList:
            adjacency_matrix[edge_object.fromNode.value][edge_object.toNode.value] = edge_object.weight
        return adjacency_matrix

    def find_max_index(self):
        max_index = -1
        if len(self.nodesList):
            for node in self.nodesList:
                if node.value > max_index:
                    max_index = node.value
        return max_index


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print (graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print (graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print (graph.get_adjacency_matrix())

aName = input("please tell me what you think")