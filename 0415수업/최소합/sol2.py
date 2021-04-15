import sys
sys.stdin = open("input.txt")

T = int(input())

def func(x, y, tmp_sum) :
    global result
    if tmp_sum > result :
        return
    elif x==(N-1) and y==(N-1) :
        if tmp_sum < result :
            result = tmp_sum
            return

    for m in move :
        next_x = x+m[0]
        next_y = y+m[1]
        if next_x<N and next_y<N :
            func(next_x,next_y,tmp_sum+inp_arr[next_y][next_x])


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    move= [ [1,0], [0,1] ] # 오른쪽/ 아래쪽
    result = 50 * 2 * N
    func(0, 0, inp_arr[0][0])

    print("#{} {}".format(tc, result))

