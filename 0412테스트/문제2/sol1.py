import sys
sys.stdin = open("문제2_input.txt")

T = int(input())

def BFS(start) :
    queue = [ start ]
    cnt = 0
    while queue :
        now_node = queue.pop(0)
        queue.extend(node_arr[now_node])
        cnt+=1
    return cnt-1 # 루트노드 한개 제외


for tc in range(1, T+1):
    V, N = map(int, input().split())
    # V : 노드의 갯수
    # N : 구하려는 노드

    inp_arr = list(map(int, input().split()))
    node_arr = [ [] for _ in range(V+1)]

    for i in range(0, len(inp_arr), 2) :
        parent, child = inp_arr[i:i+2]
        node_arr[parent].append(child)

    result = BFS(N)

    print("#{} {}".format(tc, result))

