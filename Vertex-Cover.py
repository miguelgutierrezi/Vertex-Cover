import itertools
import random

class Vertex_Cover:

    def __init__(self, graph):
        self.graph = graph

    def validity_check(self, cover):
        is_valid = True
        for i in range(len(self.graph)):
            for j in range(i+1, len(self.graph[i])):
                if self.graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                    return False

        return is_valid

    def vertex_cover_AP(self):
        C = set()
        edge_copy = self.graph.copy()
        while bool(edge_copy):
            arb_edge = edge_copy.pop()
            print (arb_edge)
            if len(arb_edge[1]) == 0:
                continue
            C.add(arb_edge[0])
            for val in arb_edge[1]:
                if arb_edge[0] in edge_copy[val]:
                    edge_copy[val].remove(arb_edge[0])
        return C

    def vertex_cover_BF(self):
        n = len(self.graph)
        minimum_vertex_cover = n
        a = list(itertools.product(*["01"] * n))
        for i in a:
            if Vertex_Cover.validity_check(ins, i):
                counter = 0
                for value in i:
                    if value == '1':
                        counter += 1
                minimum_vertex_cover = min(counter, minimum_vertex_cover)

        return minimum_vertex_cover

def random_adjacency_matrix():
    n = random.randint(4, 16)
    matrix = [[random.randint(0,1) for i in range(n)] for j in range(n)]

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(0,1)    
            matrix[i][j] = matrix[j][i]

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0
 
    return matrix

# print(graphM)
for i in range (0, 101):
    graphM = random_adjacency_matrix()
    ins = Vertex_Cover(graphM)
    print ("the minimum vertex-cover is: ", Vertex_Cover.vertex_cover_BF(ins))