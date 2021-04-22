import sys
sys.stdin = open("input.txt")

T = int(input())

def BFS(i) :
    global visited
    queue = []
    if visited[i] == 1 :
        return 0
    queue.append(i)
    visited[i]=1
    length= 0
    while queue :
        queue2 = []
        length+=1
        for point in queue :
            for j in range(1, N+1) :
                if map_arr[point][j] and not visited[j] :
                    queue2.append(j)
                    visited[j] =1
        queue = queue2
    visited = [0] * (N+1)
    return length

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

    result = [BFS(i) for i in range(1,N+1)]
    max_length = max(result)

    print("#{} {}".format(tc, max_length))

