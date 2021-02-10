import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * (Q+1)
    result = [0] * (N+1)

    for i in range(1,Q+1) :
        L, R = map(int, input().split())
        arr[i] = (L,R)

    for i in range(1,Q+1) :
        for j in range(arr[i][0], arr[i][1]+1) :
            result[j] = i

    result = map(str, result[1:])
    result = " ".join(result)
    print("#{} {}".format(tc, result))

