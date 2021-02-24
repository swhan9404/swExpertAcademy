import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    M = inp_arr[-1] # 최대값
    result = 0
    for i in range(len(inp_arr)-1, -1 ,-1) :
        if inp_arr[i]> M :
            M = inp_arr[i]

        result += M- inp_arr[i]

    print("#{} {}".format(tc, result))

