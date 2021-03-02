import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    M = inp_arr[-1] # 최대값
    result = 0
    for i in range(len(inp_arr)-1, -1 ,-1) : # 뒤에서부터 보기
        if inp_arr[i]> M : # 최대값보다 큰 것을 만나면 최대값에 넣고 정산
            M = inp_arr[i]

        result += M- inp_arr[i] # 정산하기

    print("#{} {}".format(tc, result))

