import random
import argparse

SHUFFLE = 20

def get_weight(adj_list, vertices):
    total = 0
    for v in range(len(vertices)-1):
        this = vertices[v]
        nxt = vertices[v+1]
        total += adj_list[this].get(nxt)
    return round(total, 4)

def best_permutation(adj_list, vertices):
    print('best_perm')
    weight = get_weight(adj_list, vertices) #get the weight of the vertex list as-is
    permutation = vertices

    for v in range(1, len(vertices)-1): # iterate through indices
       for u in range (v+1, len(vertices)-1): # ^ 
            if u != v: # ensure that we are not swapping matching characters
                left = vertices[u] # store left
                right = vertices[v] # store right
                vertices[v] = left # swap
                vertices[u] = right # swap
                total = get_weight(adj_list, vertices) # get weight of adjusted list
                if total < weight: # check for sol
                    weight = total # store new value
                    permutation = vertices.copy() # store ordering of vertices
                left = vertices[u] # store left
                right = vertices[v] # store right
                vertices[v] = left # swap
                vertices[u] = right # swap
    return total, permutation # return minimum weights and the order that produced it

# def best_permutation(adj_list, vertices):
#     unvisited = set(adj_list.keys())
#     unvisited.remove(vertices[0])
#     tour = [vertices[0]]
#     weight = 0


#     while unvisited:
#         curr = adj_list[tour[-1]]
#         min_dist = min(unvisited, key=lambda v: adj_list[tour[-1]].get(v))
#         unvisited.remove(min_dist)
#         weight += curr.get(min_dist)
#         tour.append(min_dist)
#     weight += adj_list[tour[-1]].get(vertices[0])
#     tour.append(vertices[0])
#     return weight, tour

def approximate(adj_list):
    smallest = float('inf') # minimum threshold
    best = [] # best permutation of vertices
    vnum = len(adj_list) # number of vertices
    v = [k for k in adj_list.keys()] # get all vertex labels
    for i in range(args.shuffle): # shuffle the order the # of times specified on cmdline (else 20)
        curr = v.copy() # make a copy and store it
        random.shuffle(curr) # shuffle order
        curr.append(curr[0]) # add the source vertex as the dest
        dist, order = best_permutation(adj_list, curr) # explore internal shufflings and store best
        if dist < smallest: # check for improved sol
            smallest = dist # store lower value
            best = order # store improved vertex order
    return smallest, best #return the minimum weight and permuation

def main(args):
    ve = input().split()
    num_vertices = int(ve[0])
    num_edges = int(ve[1])
    adj_list = {}

    for edge in range(num_edges):
        u, v, w = input().split()
        if u not in adj_list:
            adj_list[u] = {}
        if v not in adj_list:
            adj_list[v] = {}
        adj_list[u][v] = float(w)
        adj_list[v][u] = float(w)

    dist, order = approximate(adj_list)
    print(f'{dist:.4f}')
    for v in order:
        print(v, end=' ')
    print("\n")
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--shuffle', default=SHUFFLE, type=int,
                    help='The number of shuffled permutations to test.'
                            'Default: 20')
    args=parser.parse_args()

    main(args)