import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    divide_arr = [2,3,5,7,11]
    result_arr = [0]*5


    def func(N, x):
        while N != 1:
            if N % divide_arr[x]:
                break
            else:
                N //= divide_arr[x]
                result_arr[x] += 1
        return N

    for i in range(len(divide_arr)) :
        N = func(N, i)

    result_arr = map(str, result_arr)
    result = " ".join(result_arr)
    print("#{} {}".format(tc, result))

