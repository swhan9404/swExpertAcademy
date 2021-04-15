import sys
sys.stdin = open("input.txt")

T = int(input())

def func(now, cnt, tmp_sum) : # 현재위치 / 몇칸 왔는지/  현재까지의 합
    global result
    if result < tmp_sum :
        return
    elif cnt == N and now==0:
        if result > tmp_sum :
            result = tmp_sum
        return
    elif cnt == N :
        return

    for i in range(N) :
        if visited[i] == 0 and inp_arr[now][i] != 0:
            visited[i] = 1
            func(i, cnt+1, tmp_sum+inp_arr[now][i])
            visited[i] = 0


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 100* N

    func(0, 0, 0)

    print("#{} {}".format(tc, result))

