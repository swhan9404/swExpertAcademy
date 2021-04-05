# https://www.acmicpc.net/problem/12967
from math import gcd
# 완탐 풀이 - 시간초과
N, K = map(int, input().split())
inp_arr= list(map(int, input().split()))

tmp_cnt = 0
for i in range(N-1, -1, -1) :
    tmp = inp_arr[i]
    if tmp >=K and tmp%K == 0 :
        tmp_cnt +=1
        inp_arr.pop(i)

cnt = 0
N = len(inp_arr) # 줄어든걸로 다시
for i in range(N-2) :
    for j in range(i+1, N-1):
        for k in range(j+1, N) :
            tmp = gcd(inp_arr[i], K) * gcd(inp_arr[j], K) * gcd(inp_arr[k], K)

            if tmp%K == 0 :
                cnt+=1

print(cnt)