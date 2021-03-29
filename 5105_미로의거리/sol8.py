import sys
sys.stdin = open("input.txt")

from collections import deque


T = int(input())

def find_start() :
    for y in range(N) :
        for x in range(N) :
            if miro[y][x] == '2' :
                return x, y

def func(start_x, start_y) :
    queue = deque() # 큐 생성
    queue.append([start_x, start_y]) # 시작x, y, 시작점과의거리
    visited = [[0] * N for _ in range(N)]

    move_x = [1,-1,0,0] # 오른쪽, 왼쪽, 위, 아래
    move_y = [0,0,-1,1]
    ###########################차이점############################
    distance =0
    while queue : # 큐가 빌때 까지
        size = len(queue)
        for i in range(size) :
            now_x, now_y = queue.popleft()
            if miro[now_y][now_x] == '3':
                return distance - 1  # 도착지점은 길이에 포함 안되네..

            elif miro[now_y][now_x] in ['0', '2'] and visited[now_y][now_x] == 0:  # 길이고, 방문하지 않은 경우
                visited[now_y][now_x] = 1

                for i in range(4):
                    next_x = now_x + move_x[i]
                    next_y = now_y + move_y[i]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        queue.append((next_x, next_y))
        distance+=1
    ###############################################################


# BFS - 최소경로 / 실행시간 :실행 시간 : 0.15346s
for tc in range(1, T+1):


    N = int(input()) # 미로 크기
    miro = [input() for _ in range(N)]
    start_x, start_y = find_start()
    result = func(start_x, start_y)
    if result == None :
        result =0

    print("#{} {}".format(tc, result))

