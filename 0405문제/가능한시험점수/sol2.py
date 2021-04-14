import sys

sys.stdin = open("input.txt")

T = int(input())

# 완전탐색으로 풀면 시간초과
def func() :
    result_arr = [0]
    for i in range(N) :
        for j in range(len(result_arr)) :
            tmp = inp_arr[i]
            tmp2 = result_arr[j]

            if visited[tmp + tmp2] == 0 :
                visited[tmp + tmp2] = 1
                result_arr.append(tmp + tmp2)
    return result_arr


for tc in range(1, T + 1):
    N = int(input())
    inp_arr = list(map(int, input().split()))
    visited = [0] * (100 * N) # 결과값이 중복되는지 확인용
    visited[0] =1

    result_arr =func()

    print("#{} {}".format(tc, len(result_arr)))

