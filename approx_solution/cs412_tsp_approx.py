import random
import argparse

SHUFFLE = 20

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
            copy = vertices.copy() #copy temp array
            if copy[u] != copy[v]:
                left = copy[u] #store left
                right = copy[v] #store right
                copy[v] = left #swap
                copy[u] = right #swap
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
    for i in range(args.shuffle):
        curr = v.copy()
        random.shuffle(curr)
        curr.append(curr[0])
        dist, order = best_permutation(matrix, curr)
        if dist < smallest:
            smallest = dist
            best = order
    return smallest, order

def main(args):
    encodings = []
    ve = input().split()
    num_vertices = int(ve[0])
    num_edges = int(ve[1])
    adj_matrix = [[None for y in range(num_vertices)] for x in range(num_vertices)]

    start = 'a'
    for vert in range(num_vertices):
        encodings.append(start)
        start = chr(ord(start)+1)

    for edge in range(num_edges):
        u, v, w = input().split()
        adj_matrix[int(encodings.index(v))][int(encodings.index(u))] = float(w)
        adj_matrix[int(encodings.index(u))][int(encodings.index(v))] = float(w)

    dist, order = approximate(adj_matrix)
    print(dist)
    for v in order:
        print(encodings[v], end=" ")
    print()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--shuffle', default=SHUFFLE, type=int,
                    help='The number of shuffled permutations to test.'
                            'Default: 20')
    args=parser.parse_args()

    main(args)