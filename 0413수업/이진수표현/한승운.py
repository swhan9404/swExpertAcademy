import sys
sys.stdin = open("input.txt")

T = int(input())
def func(M, N) :
    for _ in range(N) :
        M, re = divmod(M,2)
        if re == 0 :
            return "OFF"
    else :
        return "ON"


for tc in range(1, T+1):
    N,M = map(int, input().split())
    result = func(M,N)

    print("#{} {}".format(tc, result))

