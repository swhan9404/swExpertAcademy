import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int,list(input()))) for _ in range(N)]

    side_start = N//2 # 빈칸 시작이 몇칸인지

    result =0
    for y in range(N) :
        side_size = abs(side_start - y) # 음수가 나올 수 있으니 절대값
        for x in range(side_size, N-side_size) :
            result+=inp_arr[y][x]

    print("#{} {}".format(tc, result))

