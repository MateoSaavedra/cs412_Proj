"""
Code to find exact solution using backtracking algorithm
"""

from itertools import product


def inDict(val, dict):
    try:
        check = dict[val]
        return True
    except KeyError:
        return False


def getPathLen(path, graph):
    pass


def getShortestCycle(graph):
    vertices = graph.keys()
    minLen = - float('inf')
    for path in product(vertices, repeat=len(vertices)):
        if len(set(path)) != len(path):
            continue
        pathLen = getPathLen(path)
        minLen = min(pathLen, minLen)
    return minLen


def main():
    line1 = input().split()
    n = int(line1[0]) # number of vertices
    m = int(line1[1]) # number of edges
    graph = {}
    for _ in range(m):
        edge = input().split()
        u = edge[0]
        v = edge[1]
        w = float(edge[2])
        if inDict(u, graph):
            graph[u][v] = w 
        else:
            graph[u] = {v : w}
        if inDict(v, graph):
            graph[v][u] = w
        else:
            graph[v] = {u : w}
    result = getShortestCycle(graph)
    print(result)


if __name__ == "__main__":
    main()