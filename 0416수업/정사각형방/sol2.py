import sys
sys.stdin = open("input.txt")

T = int(input())

def func() :
    for y in range(N) :
        for x in range(N) :
            for i in range(4) :
                next_x = x + move_x[i]
                next_y = y + move_y[i]

                if 0<=next_x<N and 0<=next_y<N and inp_arr[next_y][next_x]-inp_arr[y][x] == 1 :
                    continue_arr[inp_arr[y][x]] =1
    cnt = 1
    max_cnt = 0
    start =0
    max_start =0
    for i in range(len(continue_arr)) :
        if continue_arr[i] == 0 :

            if cnt > max_cnt :
                max_cnt = cnt
                max_start = start
            cnt =1
            start = i+1
        else :
            cnt +=1
    else :
        if cnt > max_cnt:
            max_cnt = cnt

    return max_start, max_cnt

for tc in range(1, T+1):
    N = int(input())

    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    continue_arr = [0] * (N **2 + 1) # 수가 연결되는게 있는지


    move_x = [1,-1,0,0] # 오, 왼 , 위, 아래
    move_y = [0,0,-1,1]

    start, cnt = func()

    print("#{} {} {}".format(tc, start, cnt))

