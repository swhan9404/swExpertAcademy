import sys
sys.stdin = open("input.txt")

from collections import deque
T = 10

def find_start() :
    for y in range(N) :
        for x in range(N) :
            if miro[y][x] == "2" :
                return x, y

move_x = [1,-1,0,0] # 오른쪽, 왼쪽, 위, 아래
move_y = [0,0,-1,1]

def func(start_x, start_y) :
    queue= deque()
    visited= [ [0] *N for _ in range(N) ] # 리스트로 거리 구하는거 따라해보기

    queue.append( (start_x, start_y) )
    while queue :
        now_x, now_y = queue.popleft()

        if miro[now_y][now_x] == "3" :
            return visited[now_y][now_x] # 거리 반환

        for i in range(4) :
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0<=next_x<N and 0<=next_y<N and miro[next_y][next_x] in ["0", "3"] and visited[next_y][next_x] ==0:# 길이고, 방문하지 않은거
                # 방문처리
                visited[next_y][next_x] = visited[now_y][now_x] +1
                queue.append( (next_x, next_y) )


# BFS
for tc in range(1, T+1):
    nothing = input()
    N = 16 # 미로 크기
    miro = [input() for _ in range(N)]

    start_x, start_y = find_start()
    distance = func(start_x, start_y)

    if distance : # 거리 측정 가능
        result =1
    else :
        result = 0

    print("#{} {}".format(tc, result))

