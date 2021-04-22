import sys
sys.stdin = open("input.txt")

T = int(input())

def BFS(i) :
    global cnt
    cnt+=1
    queue = [i]
    visited[i] = cnt
    while queue :
        now = queue.pop(0)
        for j in range(1, N+1) :
            if map_arr[now][j] and not visited[j] :
                queue.append(j)
                visited[j] = cnt


for tc in range(1, T+1):
    N, M = map(int, input().split())
    inp_arr = list(map(int, input().split()))
    map_arr = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(0, len(inp_arr), 2):
        sm = inp_arr[i]
        lg = inp_arr[i + 1]
        map_arr[sm][lg] = 1
        map_arr[lg][sm] = 1

    for i in range(1, N + 1):
        if not visited[i]:
            BFS(i)


    print("#{} {}".format(tc, cnt))

