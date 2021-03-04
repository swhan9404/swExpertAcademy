import sys
sys.stdin = open("input.txt")

T = int(input())

# DFS while문
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gansun_arr = [[0]* (V+1) for _ in range(V+1)] # 행 : 출발 / 열 : 도착

    for _ in range(E) :
        start, end = map(int, input().split())
        gansun_arr[start][end] = 1

    S, G = map(int, input().split()) # S: 출발 G :도착

    # DFS 개념
    visited = [0] * (V+1)
    stack = [S]
    while stack :
        now = stack.pop()
        # 방문안한 경우
        if visited[now] == 0 :
            visited[now] = 1
            # 현재 노드와 연결된 모든 노드를 반복
            for v in range(V, -1, -1) : # 먼저의 번호가 우선
                if visited[v] == 0 and gansun_arr[now][v]==1:
                    stack.append(v)

    result = 1 if visited[G] else 0

    print("#{} {}".format(tc, result))

