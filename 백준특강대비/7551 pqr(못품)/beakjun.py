# https://www.acmicpc.net/problem/12967

# 완탐 풀이 - 시간초과
N, K = map(int, input().split())
inp_arr= list(map(int, input().split()))

cnt = 0
for i in range(N-2) :
    for j in range(i+1, N-1):
        for k in range(j+1, N) :
            tmp = inp_arr[i] * inp_arr[j] *inp_arr[k]
            if tmp%K == 0 :
                cnt+=1

print(cnt)