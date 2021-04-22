import sys
sys.stdin = open("input.txt")

T = int(input())
def DFS(start, length) :
    global max_length
    if length > max_length :
        max_length = length

    for i in range(1,N+1) :
        if map_arr[start][i] and not visited[i] :
            visited[i] = 1
            DFS(i, length+1)
            visited[i] = 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 정점 수
    # M : 간선 수
    map_arr = [[0] * (N+1) for _ in range(N+1) ]
    visited= [0] * (N+1)
    for _ in range(M) :
        start, end = map(int, input().split())
        map_arr[start][end] =1
        map_arr[end][start] =1

    max_length = 0
    for i in range(1, N+1) :
        DFS(i, 0)
        visited = [0] * (N+1)
    max_length = max_length if max_length else 1
    print("#{} {}".format(tc, max_length))

