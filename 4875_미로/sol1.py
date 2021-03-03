import sys
sys.stdin = open("input.txt")

T = int(input())

move_x = (1,-1,0,0)# 오른쪽, 왼쪽, 위, 아래
move_y = (0,0,-1,1)

for tc in range(1, T+1):
    N = int(input())
    miro = [input() for _ in range(N)]
    visited = [ [0] * N for _ in range(N)]
    result =0

    def find_start() : # 시작 위치 찾기
        for y in range(N) :
            for x in range(N) :
                if miro[y][x] == "2" :
                    return x,y

    def move(x,y) : # 점을 움직이면서 방문처리 하기
        global result
        if not(0<=x<N) or not(0<=y<N) or miro[y][x] == "1" or visited[y][x]==1:
            return
        elif miro[y][x] == "3" :
            result = 1
            return

        visited[y][x] =1 # 방문처리
        for i in range(4) :
            dx = move_x[i]
            dy = move_y[i]
            move(x+dx, y+dy)

    start_pt_x, start_pt_y = find_start()
    move(start_pt_x, start_pt_y)

    print("#{} {}".format(tc, result))

