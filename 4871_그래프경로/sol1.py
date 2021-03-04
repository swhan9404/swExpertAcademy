import sys
sys.stdin = open("input.txt")

T = int(input())

# DFS, BFS 풀이 x / 모든 경로 찾기
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gansun_arr = [[0]* (V+1) for _ in range(V+1)] # 행 : 출발 / 열 : 도착

    for _ in range(E) :
        start, end = map(int, input().split())
        gansun_arr[start][end] = 1

    S, G = map(int, input().split()) # S: 출발 G :도착

    visited = [0] * (V+1)
    result = 0
    def func(now) : # 출발점
        global result
        if now == G :
            result = 1
        elif visited[now] : # 방문한적이 있으면
            return

        for i in range(1, V+1) :
            if gansun_arr[now][i] == 1 and visited[i]==0: # 이어진 간선이 있고 그 점을 방문하지 않은 경우
                visited[now] = 1 # 현재 위치를 갔다고 표시
                func(i) # 다음 위치 이동
                visited[now] = 0 # 현재 위치 비방문 처리

    func(S)
    print("#{} {}".format(tc, result))

