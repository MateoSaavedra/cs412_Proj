"""
Code to find exact solution to TSP using backtracking algorithm
"""

from itertools import permutations


def inDict(val, dict):
    try:
        check = dict[val]
        return True
    except KeyError:
        return False


"""
Return the length of the path
"""
def getPathLen(path, graph):
    total_length = 0
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        
        # Check for edge
        if v in graph.get(u, {}):
            total_length += graph[u][v]
        else:
            # Edge does not exist
            return 100000
    
    # Add return edge to form a cycle
    if path[-1] in graph.get(path[0], {}):
        total_length += graph[path[-1]][path[0]]
    else:
        return float('inf')
    
    return total_length


def getShortestCycle(graph):
    vertices = graph.keys()
    minLen = float('inf')
    minPath = 0
    for path in permutations(vertices):
        pathLen = getPathLen(path, graph)
        if pathLen < minLen:
            minPath = path
            minLen = pathLen
    return (minLen, minPath)


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

    min_len, min_path = getShortestCycle(graph)
    print(f"{min_len:.4f}")
    path_str = " ".join(min_path) + " " + min_path[0]
    print(path_str)


if __name__ == "__main__":
    main()