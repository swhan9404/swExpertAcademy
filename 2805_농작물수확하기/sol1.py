import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int,list(input()))) for _ in range(N)]

    side_start = N//2

    result =0
    for y in range(N) :
        side_size = abs(side_start - y)
        for x in range(side_size, N-side_size) :
            result+=inp_arr[y][x]

    print("#{} {}".format(tc, result))

