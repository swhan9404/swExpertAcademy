import sys
sys.stdin = open("input.txt")

T = int(input())

def tree_size(N, child_arr) :
    queue = [N]
    size = 0
    while queue :
        queue2= []
        for tmp in queue :
            queue2.extend(child_arr[tmp])
        size+=len(queue)
        queue = queue2
    return size

for tc in range(1, T+1):

    E, N = map(int,input().split())
    inp_arr = list(map(int, input().split()))
    child_arr = [[] for _ in range(E+2)]

    for i in range(0, len(inp_arr), 2) :
        child_arr[ inp_arr[i] ].append(inp_arr[i+1])

    result = tree_size(N, child_arr)

    print("#{} {}".format(tc, result))

