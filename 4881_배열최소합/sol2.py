import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))

    def func_sum(prefix) :
        tmp_result = 0
        for y in range(len(prefix)) :
            tmp_result += inp_arr[y][ prefix[y] ]
        return tmp_result

    def func(prefix, k) :
        tmp_result = func_sum(prefix)
        global result
        if result<tmp_result :
            return
        elif len(prefix) == N :
            result = tmp_result
            return
        else :
            for i in range(k, len(arr)) :
                arr[i], arr[k] = arr[k], arr[i]
                func(prefix+[arr[k]], k+1)
                arr[i], arr[k] = arr[k], arr[i]

    result = 50*N # 최댓값 * 갯수
    func([], 0)


    print("#{} {}".format(tc, result))

