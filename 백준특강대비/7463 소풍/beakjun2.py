# 단순구현 2
# 시간초과 여전

N, K, M = map(int, input().split())

arr = list(range(1, N+1))

def func(arr, K, M) :
    start_len = len(arr)
    cnt = 0
    while True :
        cnt = (cnt + K -1) % len(arr)
        now = arr.pop(cnt)
        if now == M :
            return start_len - len(arr)


print(func(arr, K, M))