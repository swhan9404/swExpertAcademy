import sys
sys.stdin = open("input.txt")

T = int(input())

def dijkstra(now_x, map_arr, dis_go, visited) :
    x = now_x
    while True :
        visited[x] = 1
        now_dis = dis_go[x]
        min_dis = INF
        min_idx = 0

        for i in range(1, N+1) :
            if not visited[i] and map_arr[x][i] and now_dis+map_arr[x][i]<dis_go[i] :
                dis_go[i] = now_dis+map_arr[x][i]

        for i in range(1, N+1) :
            if not visited[i] and min_dis > dis_go[i] :
                min_dis = dis_go[i]
                min_idx = i
        if min_idx :
            x = min_idx
            continue
        return

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    map_arr = [[0]*(N+1) for _ in range(N+1)]
    map_arr_reverse = [[0]*(N+1) for _ in range(N+1)]
    INF = 9876543210
    dis_go = [INF]*(N+1)
    dis_back = [INF]*(N+1)
    dis_go[X] = 0
    dis_back[X] = 0

    for _ in range(M) :
        x, y, c = map(int, input().split())
        map_arr[x][y] = c
        map_arr_reverse[y][x] =c

    visited=[0]* (N+1)
    dijkstra(X, map_arr, dis_go, visited)
    visited = [0] * (N + 1)
    dijkstra(X, map_arr_reverse, dis_back, visited)
    result = 0

    for i in range(1, N+1) :
        tmp_sum = dis_go[i] + dis_back[i]
        if i!=X and tmp_sum > result :
            result = tmp_sum

    print("#{} {}".format(tc, result))

