import sys

sys.stdin = open("input.txt")

T = int(input())


def find_start():
    for y in range(N):
        for x in range(N):
            if miro[y][x] == '2':
                return x, y


move_x = [1, -1, 0, 0]  # 오른쪽, 왼쪽, 위, 아래
move_y = [0, 0, -1, 1]


def func(now_x, now_y, distance):
    global result
    if miro[now_y][now_x] == '3':  # 도착하면 지금까지 구한 거리랑 비교
        if (distance - 1) < result:
            result = distance - 1
        return
    elif distance > result : # 중단 조건 추가
        return

    distance += 1
    for i in range(4):
        next_x = now_x + move_x[i]
        next_y = now_y + move_y[i]
        if 0 <= next_x < N and 0 <= next_y < N and miro[next_y][next_x] in ['0', '3'] and visited[next_y][next_x] == 0:  # 길이고, 방문하지 않은 경우:
            visited[next_y][next_x] = 1
            func(next_x, next_y, distance)
            visited[next_y][next_x] = 0



# 모든 경로 구하고 최소값으로 구하기 / 실행 시간 : 0.12256s
for tc in range(1, T + 1):
    N = int(input())  # 미로 크기
    miro = [input() for _ in range(N)]
    start_x, start_y = find_start()

    visited = [[0] * N for _ in range(N)]
    result = N ** 2
    func(start_x, start_y, 0)

    if result == N ** 2:  # 초기값에서 변화가 없을 경우 도착 못한것
        result = 0

    print("#{} {}".format(tc, result))

