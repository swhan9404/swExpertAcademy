import sys
sys.stdin = open("input.txt")

T = int(input())

def get_parent(x) :
    if parent[x] != x :
        parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(x, y) :
    x_par = get_parent(x)
    y_par = get_parent(y)
    if x_par > y_par :
        parent[x_par] = y_par
    else :
        parent[y_par] = x_par

def find(x,y) :
    return get_parent(x) == get_parent(y)

def kruskal() :
    global result
    while inp_arr :
        start, end, val = inp_arr.pop()
        if not find(start, end) :
            union_parent(start, end)
            result += val

for tc in range(1, T+1):
    V, E = map(int, input().split())
    inp_arr = [list(map(int, input().split())) for _ in range(E)]
    inp_arr.sort(key=lambda x : -x[2])

    parent = [i for i in range(V+1)]
    result =0
    kruskal()

    print("#{} {}".format(tc, result))

