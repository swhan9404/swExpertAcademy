import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 정수의 갯수
    # M : 구간의 갯수
    N, M = map(int, input().split())
    # 정수 리스트  N개
    inp_arr = list(map(int, input().split()))

    min_ = 10000 * M # 정수 최대값 * 구간길이
    max_ = 0

    for i in range(N-M+1) :
        tmp =0
        for j in range(M) :
            tmp += inp_arr[i+j]

        if  tmp< min_:
            min_ = tmp
        if tmp > max_:
            max_ = tmp

    print("#{} {}".format(tc, max_-min_))

