import sys
sys.stdin = open("문제3_input.txt")

T = int(input())

def find_target(target) :
    for y in range(N) :
        for x in range(N) :
            if inp_arr[y][x] == target :
                inp_arr[y][x] = 0 # 맵에 0 으로 초기화시켜주기

                return x,y


move_x = [0,0,-1,1] # 상하좌우
move_y = [-1,1,0,0]

def BFS(start) :
    queue = [start]
    start_x, start_y = start
    visited[start_y][start_x] = 1
    cnt = 0
    while queue :
        cnt +=1 # 움직인 거리
        queue2 = []
        while queue :
            now_x, now_y = queue.pop(0)
            for i in range(4) : # 움직이기
                next_x = now_x + move_x[i]
                next_y = now_y + move_y[i]

                if 0<=next_x<N and 0<=next_y<N and visited[next_y][next_x] == 0 and inp_arr[next_y][next_x] ==0: # 판못나가게 / 방문안한거 / 벽아닌곳
                    for j in range(3) : # Zone 체크
                        zone_x, zone_y = zones[j]
                        if zones_visited[j]==0 and next_x == zone_x and next_y == zone_y : # 방문안한 Zone 방문
                            zones_visited[j] = 1 # zone 방문처리
                            inp_arr[zone_y][zone_x] = 1 # zone 다시 못지나가게
                            return cnt, (zone_x, zone_y) # 이동거리, 다음 시작점 반환
                    visited[next_y][next_x] = 1 # 다음 위치 방문처리
                    queue2.append((next_x, next_y)) # queue2 에 넣기
        queue = queue2
    else : # 아무곳도 도착못할경우
        return 0, (0, 0)

for tc in range(1, T+1):
    N = int(input())

    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    # 0 빈칸
    # 1 벽
    # 2 로봇
    # 3 Red Zone
    # 4 Green Zone
    # 5 Blue Zone
    robot = list(find_target(2))
    zones = [list(find_target(x)) for x in range(3, 6)]

    zones_visited = [0] * 3
    result = 0

    for _ in range(3) :
        visited = [[0] * N for _ in range(N)]
        tmp_cnt, robot = BFS(robot)
        if tmp_cnt == 0 : # 아무곳도 못간경우 탈출
            break
        result += tmp_cnt

    print("#{} {}".format(tc, result))

