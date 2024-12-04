import random 

def generate(v, case_num):
    filename = f"test{case_num}.txt"
    file = open(filename, 'w')

    used = set()
    label  = 'a'
    edges = v*(v-1)//2
    vertices = ['a']

    file.write(f"{v} {edges}\n")
    for v in range(v-1):
        print(label)
        if label[-1] == 'z':
            label = label[:-1] + 'aa'
        else:
            label = label[:-1] + chr(ord(label[-1])+1)
        vertices.append(label)
    for v in vertices:
        for u in vertices:
            if v != u and (v, u) not in used and (u, v) not in used:
                used.add((v, u))
                file.write(f"{v} {u} {round(random.uniform(1, 10), 1)}\n")
    file.close()

def main():
    num_graphs = int(input())
    for g in range(1, num_graphs):
        generate(random.randint(4, 10), g)
    generate(1010, num_graphs)

if __name__ == '__main__':
    main()