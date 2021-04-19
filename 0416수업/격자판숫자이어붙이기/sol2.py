import sys
sys.stdin = open("input.txt")

T = int(input())


def func(x,y, k) :
    result[k] = inp_arr[y][x]
    if k == 6 :
        visited["".join(result)] = 1
        return

    for i in range(4) :
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0<=next_x<N and 0<=next_y<N :
            func(next_x, next_y, k+1)


for tc in range(1, T+1):
    N=4
    inp_arr = [input().split() for _ in range(N)]
    move_x = [1,-1,0,0] # 오른쪽, 왼쪽, 위, 아래
    move_y = [0,0,-1,1]
    visited = {}

    result = [0] * 7
    for i in range(N) :
        for j in range(N) :
            func(i, j, 0)


    print("#{} {}".format(tc, len(visited)))

