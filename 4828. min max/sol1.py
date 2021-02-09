import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    if N == 0 :
        continue

    max_ = inp_arr[0]
    min_ = inp_arr[0]

    for tmp in inp_arr :
        if tmp > max_ :
            max_ = tmp

        if tmp < min_ :
            min_ = tmp

    print("#{} {}".format(tc, max_-min_))

