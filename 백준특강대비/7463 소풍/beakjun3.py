# 단순구현 2
# 시간초과 여전

N, K, M = map(int, input().split())

def func(N, K, M) :
    start_len = N
    cnt = 0
    tmp_len =start_len
    while True :
        cnt = (cnt + K -1) % tmp_len
        tmp_len -=1

        if cnt == M -1 :
            return start_len - tmp_len


print(func(N, K, M))