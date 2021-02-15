import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    result_arr = [[0]*N for _ in range(N)]

    # 오른쪽 아래 왼쪽 위쪽
    move_x = (1,0,-1,0)
    move_y = (0,1,0,-1)

    start_x, start_y = 0, 0
    move_direction=0
    def func(cnt, x, y, move_direction) :
        if cnt > N**2 :
            return

        result_arr[y][x] = cnt

        dx = x+ move_x[move_direction]
        dy = y+ move_y[move_direction]

        if not(0<=dx<N) or not(0<=dy<N) or result_arr[dy][dx]!=0 :
            move_direction +=1
            move_direction %=4

            dx = x + move_x[move_direction]
            dy = y + move_y[move_direction]

        func(cnt+1, dx, dy, move_direction)

    func(1,0,0,0)

    print("#{}".format(tc))
    for y in range(N) :
        print(*result_arr[y])
