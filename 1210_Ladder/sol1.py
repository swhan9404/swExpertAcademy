import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    tc = int(input())

    N = 100 # 판사이즈
    inp_arr = [0] * N
    for i in range(N) :
        inp_arr[i] = list(map(int, input().split()))

    move_x = [1,-1,0] # 오른쪽, 왼쪽, 상
    move_y = [0,0,-1]

    end_pt_x = 0
    end_pt_y = N-1

    # 도착지점 찾기
    for i in range(N) :
        if inp_arr[N-1][i] == 2 :
            end_pt_x = i
            break


    # 위로 거슬러 올라가며 시작점 찾기
    def func(x, y, pattern) :
        # x,y : 현재 위치
        # pattern : 이전 움직인 방향
        if y == 0 : # 시작 위치 찾아서 반환
            return x

        # 이전에 옆으로 움직였으면 위로 가는게 우선, 아니면 옆으로 가는게 우선 - 아니면 좌우 무한 순회할수 있음
        if pattern ==2 : # 이전 위로
            move = range(3)
        elif pattern == 1 : # 이전 왼쪽
            move = [1,2,0]
        elif pattern == 0 : # 이전 오른쪽
            move = [0,2,1]

        for i in move :
            dx = x + move_x[i]
            dy = y + move_y[i]

            if (0<=dx<N) and (0<=dy<N) and inp_arr[dy][dx] == 1 : # 우선순위에 따라 체크후 거슬러올라가기
                return func(dx,dy,i)

    result = func(end_pt_x, end_pt_y,0)

    print("#{} {}".format(tc, result))

