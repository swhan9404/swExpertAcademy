# https://www.acmicpc.net/problem/11399

N = int(input())
inp_arr = list(map(int, input().split()))

inp_arr.sort()
for i in range(1,N) :
    inp_arr[i] = inp_arr[i]+inp_arr[i-1]

print("{}".format(sum(inp_arr)))