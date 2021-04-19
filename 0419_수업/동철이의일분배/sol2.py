import sys
sys.stdin = open("input.txt")

T = int(input())

def func(cnt, tmp_result) :
    global result
    if tmp_result <= max_visited[-2] :
        return    
    elif tmp_result <= max_visited[cnt] :
        return
    elif cnt == N :
        max_visited[cnt] = tmp_result
        return
    else :
        max_visited[cnt] = tmp_result


    for i in range(N) :
        if visited[i] != 1 :
            visited[i] = 1
            func(cnt+1, tmp_result*inp_arr[cnt][i]/100)
            visited[i] = 0



for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    visited =[0] * N
    max_visited= [0] * (N+2)
    func(0, 100)
    print(max_visited)
    
    print("#{} {:.6f}".format(tc, max_visited[-2]))

