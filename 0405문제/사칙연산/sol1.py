import sys
sys.stdin = open("input.txt")

T = 10


def func(n, inp_arr) : # n : 몇번 정점인지
    tmp = inp_arr[int(n)]
    if len(tmp) == 2: # leaf일 경우
        return int(tmp[1])
    else :
        if tmp[1] == "+" :
            return func(tmp[2], inp_arr) + func(tmp[3], inp_arr)
        elif tmp[1] == "-" :
            return func(tmp[2], inp_arr) - func(tmp[3], inp_arr)
        elif tmp[1] == "*":
            return func(tmp[2], inp_arr) * func(tmp[3], inp_arr)
        elif tmp[1] == "/":
            return func(tmp[2], inp_arr) / func(tmp[3], inp_arr)

for tc in range(1, T+1):
    N = int(input())
    inp_arr = [0] * (N+1)
    for _ in range(N) :
        tmp = input().split()
        inp_arr[int(tmp[0])] = tmp

    result = int(func(1, inp_arr))

    print("#{} {}".format(tc, result))

