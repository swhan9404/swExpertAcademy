import sys
sys.stdin = open("input.txt")

T = int(input())

def func(start) :
    if visited[start] == 1 :
        return

    visited[start] = 1 # 방문처리
    for next in range(V+1) :
        if gansun_arr[start][next] == 1 :
            func(next)

# DFS 재귀
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gansun_arr = [[0]* (V+1) for _ in range(V+1)] # 행 : 출발 / 열 : 도착

    for _ in range(E) :
        start, end = map(int, input().split())
        gansun_arr[start][end] = 1

    S, G = map(int, input().split()) # S: 출발 G :도착

    visited = [0] * (V+1)
    func(S)
    result = 1 if visited[G] else 0
    print("#{} {}".format(tc, result))

