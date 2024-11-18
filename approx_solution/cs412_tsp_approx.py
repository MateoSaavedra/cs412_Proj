import random
def get_weight(matrix, vertices):
    total = 0
    for v in range(len(vertices)-1):
        this = vertices[v]
        nxt = vertices[v+1]
        total += matrix[this][nxt]
    return total

def best_permutation(matrix, vertices):
    weight = get_weight(matrix, vertices)
    permutation = vertices

    for v in range(1, len(vertices)-1):
       for u in range (1, len(vertices)-1):
            copy = vertices.copy()
            if copy[u] != copy[v]:
                print(copy)
                print(u)
                print(v)
                uind = copy.index(copy[u])
                vind = copy.index(copy[v])
                print(uind)
                print(vind)
                copy[uind] = v
                copy[vind] = u
                print(copy)
                total = get_weight(matrix, copy)
                if total < weight:
                    weight = total
                    permutation = copy
    return total, permutation

def approximate(matrix):
    smallest = float('inf')
    best = []
    vnum = len(matrix)
    v = [i for i in range(vnum)]
    for i in range(20):
        curr = v.copy()
        random.shuffle(curr)
        curr.append(curr[0])
        dist, order = best_permutation(matrix, curr)
        if dist < smallest:
            smallest = dist
            best = order
    return smallest, order

def main():
    encodings = {}
    start = 'a'
    ve = input().split()
    num_vertices = int(ve[0])
    num_edges = int(ve[1])
    adj_matrix = [[None for y in range(num_vertices)] for x in range(num_vertices)]

    for vert in range(num_vertices):
        encodings[start] = vert
        start = chr(ord(start) + 1)

    for edge in range(num_edges):
        u, v, w = input().split()
        adj_matrix[int(encodings[u])][int(encodings[v])] = float(w)
        adj_matrix[int(encodings[v])][int(encodings[u])] = float(w)

    dist, order = approximate(adj_matrix)
    print(dist)
    print(order)

if __name__ == '__main__':
    main()