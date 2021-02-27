import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 손님 수
    # M : K개를 만드는데 걸리는 시간
    # K : 한번에 만드는 붕어빵 갯수
    N, M, K = map(int, input().split())
    # 손님이 오는 타이밍
    inp_arr = list(map(int, input().split()))


    # 퀵정렬
    def quickSort(inp_arr):
        if len(inp_arr) <= 1:
            return inp_arr

        pivot = inp_arr[0]
        left = []
        right = []
        same = [pivot]
        for i in range(1, len(inp_arr)):
            tmp = inp_arr[i]
            if tmp > pivot:
                right.append(tmp)
            elif tmp < pivot:
                left.append(tmp)
            else:
                same.append(tmp)
        return [*quickSort(left), *same, *quickSort(right)]


    # 정렬
    inp_arr = quickSort(inp_arr)

    for idx, tmp in enumerate(inp_arr):
        now = (tmp // M) * K - idx  # 현재 구워져 있는 붕어빵 갯수
        if now <= 0:
            result = "Impossible"
            break
    else :
        result = "Possible"

    print("#{} {}".format(tc, result))

