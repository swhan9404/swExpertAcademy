import sys
sys.stdin = open("input.txt")

T = int(input())

def dijestra(x) :
    visited[x] = 1
    now_dis = dis_arr[x]
    for i in range(N+1) :
        if not visited[i] and map_arr[x][i] and now_dis+map_arr[x][i]<dis_arr[i] :
            dis_arr[i] = now_dis+map_arr[x][i]
    min_val = 9876543210
    min_idx = 0
    for i in range(N+1) :
        if not visited[i] and min_val > dis_arr[i] :
            min_val = dis_arr[i]
            min_idx = i
    if min_idx :
        dijestra(min_idx)

for tc in range(1, T+1):
    N, E = map(int, input().split())
    map_arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E) :
        x, y, v = map(int, input().split())
        map_arr[x][y] = v
    visited = [0] * (N+1)
    dis_arr = [9876543210] * (N+1)
    dis_arr[0] = 0

    dijestra(0)

    print("#{} {}".format(tc, dis_arr[-1]))

