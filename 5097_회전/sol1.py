import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())

    # list로 queue 구현
    inp_arr= list(map(int, input().split()))

    for _ in range(M) :
        front = inp_arr.pop(0)
        inp_arr.append(front)

    result = inp_arr[0]
    print("#{} {}".format(tc, result))

