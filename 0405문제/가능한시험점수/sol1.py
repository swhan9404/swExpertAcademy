import sys
sys.stdin = open("input.txt")

T = int(input())
# 완전탐색으로 풀면 시간초과

def func(n, result) : # 몇번째까지 왔는지
    result_arr.add(result)
    if n ==N :
        return

    func(n+1, result)
    func(n+1, result+inp_arr[n])


for tc in range(1, T+1):

    N = int(input())
    inp_arr = list(map(int, input().split()))
    result_arr = set()
    func(0 , 0)
    
    print("#{} {}".format(tc, len(result_arr)))

