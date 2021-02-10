import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    # A가 항상 더 긴 배열로 만들기
    diff_len = len(A_arr) - len(B_arr)
    if diff_len <0 :
        A_arr, B_arr = B_arr, A_arr
        diff_len = -diff_len

    def func(start) : # 블럭값
        result=0
        for i in range(len(B_arr)) :
            result += A_arr[start+i] * B_arr[i]
        return result

    # 곱셈한 최대값
    result = func(0)

    for i in range(diff_len+1) :
        tmp = func(i)
        if result < tmp :
            result = tmp

    print("#{} {}".format(tc, result))

