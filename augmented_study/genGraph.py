import random

"""
Generate a complete undirected graph
edges do not repeat
"""
def generateRandomGraph():
    f = open("graph", 'w')
    n = random.randint(1, 10) # random up to 10 vertices
    verts = [chr(i) for i in range(65, 65 + n)]
    edges = set()
    graph = []
    f.write(f"{n} ")
    for v in verts:
        for u in verts:
            if v == u or (v, u) in edges or (u, v) in edges:
                continue
            weight = random.uniform(0.1, 20.0)
            edges.add( (v, u) )
            graph.append([v, u, weight])
    f.write(f"{len(graph)}\n")
    for e in graph:
        v = e[0]
        u = e[1]
        w = e[2]
        f.write(f"{v} {u} {w}\n")
    f.close()


if __name__ == "__main__":
    generateRandomGraph()