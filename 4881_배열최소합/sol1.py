import sys
sys.stdin = open("input.txt")

T = int(input())

# 제한 시간 초과
for tc in range(1, T+1):
    N = int(input())
    inp_arr = [ list(map(int, input().split())) for _ in range(N)]

    def permutation(prefix, k) :
        if len(prefix) == N :
            yield prefix
        else :
            for i in range(k, len(arr)) :
                arr[i], arr[k] = arr[k], arr[i]
                for next in permutation(prefix+ [arr[k]], k+1) :
                    yield next
                arr[i], arr[k] = arr[k], arr[i]


    arr = list(range(N))
    result = 50*N # 최대값 * 갯수
    for perm in permutation([], 0) : # permutition 경우 전부 돌면서
        tmp_sum = 0
        for y in range(N) :
            tmp_sum+=inp_arr[y][perm[y]]
            if tmp_sum> result :
                break

        if result > tmp_sum :
            result = tmp_sum

    print("#{} {}".format(tc, result))

