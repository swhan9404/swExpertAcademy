import sys
sys.stdin = open("input.txt")

T = int(input())

move_x = [1, -1, 0, 0, 1, 1, -1, -1]  # 오른쪽, 왼쪽, 위, 아래, 대각선1시, 대각선5시, 대각선7시, 대각선10시
move_y = [0, 0, -1, 1, -1, 1, 1, -1]

def check(color, x, y) : # 색깔 놓고 뒤집기
    pan[y][x]=color
    for i in range(8) : # 방향 인덱스
        k = 0 # while문 반복횟수
        while True :
            dx = x+move_x[i] * (k+1)
            dy = y+move_y[i] * (k+1)
            if  not(0<=dx<N) or not(0<=dy<N) :
                break
            elif pan[dy][dx] in [color, 0] : #같은색이거나 빈칸이면
                break
            k+=1

        if k>= 1 :
            dx = x+move_x[i] * (k+1)
            dy = y+move_y[i] * (k+1)
            if not(0<=dx<N) or not(0<=dy<N) :
                continue
            elif pan[dy][dx] == color :
                for j in range(1, k+1) :
                    dx2 = x + move_x[i] * j
                    dy2 = y + move_y[i] * j
                    pan[dy2][dx2] = color




for tc in range(1, T+1):
    N, M = map(int, input().split())

    pan = [[0] * N for _ in range(N)]

    # 초기세팅
    center = N//2 -1
    pan[center][center] = "W"
    pan[center+1][center+1] = "W"
    pan[center][center+1] = "B"
    pan[center+1][center] = "B"

    for i in range(M) :
        dol_y, dol_x, color = map(int, input().split())
        if color % 2 : # 흑돌차례
            check("B", dol_x-1,dol_y-1)
        else : # 백돌차례
            check("W", dol_x-1, dol_y-1)

    black_cnt =0
    for y in range(N) :
        for x in range(N) :
            if pan[y][x] == "B" :
                black_cnt +=1
    white_cnt = 0
    for y in range(N) :
        for x in range(N) :
            if pan[y][x] == "W" :
                white_cnt +=1

    print("#{} {} {}".format(tc, black_cnt, white_cnt))

