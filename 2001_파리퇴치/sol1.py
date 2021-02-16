import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 판크기
    # M : 파리영역 크기
    N, M = map(int, input().split())

    inp_arr =[0] * N
    for i in range(N) :
        inp_arr[i] = list(map(int, input().split()))

    # area 만들어주기
    area_x = [x for x in range(M)] * M
    area_y = []
    for y in range(M) :
        area_y += [y] * M

    result = 0
    for y in range(N-M+1) :
        for x in range(N-M+1) :
            tmp_sum =0
            for i in range(len(area_x)) : # area 돌면서 더하기
                dx = x + area_x[i]
                dy = y + area_y[i]
                tmp_sum+= inp_arr[dy][dx]

            if tmp_sum > result :
                result = tmp_sum



    print("#{} {}".format(tc, result))

