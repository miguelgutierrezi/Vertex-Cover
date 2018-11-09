import string
import random

def random_graph():

    vertex = list([])
    edges = {}

    cant = random.randint(4,16)
        
    for i in range(cant):
        vertex.add(random.choice(string.ascii_lowercase))

    for v in vertex:
        if not (v in edges):
            edges[v] = []

    for start in vertices:
        if not (start in edges):
            edges[start] = []
        no_of_edges = int(num_ver * random.random())
        for i in range(0, no_of_edges):
            new = random.choice(list(vertices))
            if new == start:
                continue
            if new not in edges[start]:
                edges[start].append(new)
                edges[new].append(start)
                
    G = Graph(vertices, edges)
    return G