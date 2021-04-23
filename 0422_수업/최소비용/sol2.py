import sys
sys.stdin = open("input.txt")

T = int(input())

def DFS(x,y, tmp_sum, before_layer) : # 백트래킹
    global min_sum
    if tmp_sum >= min_sum:
        return
    elif x == N-1 and y == N-1 :
        min_sum = tmp_sum
        return

    for i in range(4) :
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0<=next_x<N and 0<=next_y<N and not visited[next_y][next_x] :
            visited[next_y][next_x] =1
            DFS(next_x, next_y, tmp_sum+1+max(inp_arr[next_y][next_x]-before_layer,0), inp_arr[x][y])
            visited[next_y][next_x] =0

for tc in range(1, T+1) :
    N = int(input())
    inp_arr= [list(map(int, input().split())) for _ in range(N)]
    visited=[[0]* N for _ in range(N)]
    min_sum = 9876543210
    move_x = [1,-1,0,0] # 오, 왼, 위, 아래
    move_y = [0,0,-1,1]

    DFS(0,0,0,inp_arr[0][0])
    
    print("#{} {}".format(tc, min_sum))

