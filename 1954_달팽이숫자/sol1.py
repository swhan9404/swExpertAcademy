import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    result_arr = [[0]*N for _ in range(N)]

    # 오른쪽 아래 왼쪽 위쪽
    move_x = (1,0,-1,0)
    move_y = (0,1,0,-1)

    start_x, start_y = 0, 0 # 현재 위치 기억
    move_direction=0 # 현재 방향 기억

    def func(cnt, x, y, move_direction) : # cnt, 위치, 방향
        if cnt > N**2 : # cnt 가 N**2 넘어가면 종료
            return

        result_arr[y][x] = cnt # 위치에 cnt 적기

        # 다음꺼 위치 구하기
        dx = x+ move_x[move_direction]
        dy = y+ move_y[move_direction]

        # 다음 위치가 에러나면 방향 바꾸고 다시 위치 조정
        if not(0<=dx<N) or not(0<=dy<N) or result_arr[dy][dx]!=0 :
            move_direction +=1
            move_direction %=4

            dx = x + move_x[move_direction]
            dy = y + move_y[move_direction]

        # 재귀
        func(cnt+1, dx, dy, move_direction)

    # cnt=1 위치 0,0 방향 0 시작
    func(1,0,0,0)

    print("#{}".format(tc))
    for y in range(N) :
        print(*result_arr[y])
