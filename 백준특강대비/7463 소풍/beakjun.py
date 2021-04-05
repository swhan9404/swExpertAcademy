# https://www.acmicpc.net/problem/1242
# 시간 초과 - 단순구현

N, K, M = map(int, input().split())

arr = list(range(1, N+1))

def func(arr, K, M) :
    start_len = len(arr)
    cnt = 0
    while True :
        now = arr.pop(0)
        cnt+=1
        if cnt % K == 0 :
            if now == M :
                return start_len - len(arr)
        else :
            arr.append(now)

print(func(arr, K, M))