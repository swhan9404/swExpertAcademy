# https://www.acmicpc.net/problem/13706
# sqrt 쓰면 에러남(입력 수가 너무 커서)

# 이분탐색
n = int(input())
low = 1
high = n

while 1:
    mid = (low + high) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        high = mid - 1
    elif mid ** 2 < n:
        low = mid + 1