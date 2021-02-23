import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    tc, route_num = map(int, input().split())
    route = [[0]* 100 for _ in range(100)]  # 행 : 출발 / 열 : 도착
    visited = [0] * 100

    inp = input().split()
    for i in range(0,len(inp),2) :
        start, end = map(int,inp[i:i+2])
        route[start][end] = 1

    stack = []
    now = 0
    end = 99
    result = 0

    while True :
        if now == end : # 99 에 도착하면 반복종료
            result =1
            break
        visited[now] = 1 # 방문처리
        # 방문 안한 인접 정점이 있는지 확인
        for i in range(100) :
            if route[now][i]==1 and visited[i] != 1:
                stack.append(now)
                now = i
                break
        else :
            if stack : # 스택이 비어있지 않다면
                now = stack.pop()
            else :
                break

    print("#{} {}".format(tc, result))

