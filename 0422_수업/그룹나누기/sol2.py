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
        for children in child[now] :
            if not visited[children] :
                queue.append(children)
                visited[children] = cnt


for tc in range(1, T+1):
    N, M = map(int, input().split())
    inp_arr = list(map(int, input().split()))
    child = [[] for _ in range(N+1)]  # 항상 작은걸 부모로 하고, 자식들의 리스트를 가지고 있음
    visited = [0] * (N+1)
    cnt = 0
    for i in range(0, len(inp_arr),2) :

        sm = inp_arr[i]
        lg = inp_arr[i+1]
        if lg < sm :
            sm, lg = lg, sm
        child[sm].append(lg)

    for i in range(1, N+1) :
        if not visited[i] :
            BFS(i)
    # print(visited)
    print("#{} {}".format(tc, cnt))

