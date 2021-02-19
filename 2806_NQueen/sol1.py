import sys
sys.stdin = open("input.txt")

T = int(input())

# 못품
for tc in range(1, T+1):
    N = int(input())

    move_x = (1,2,-1,-2)
    move_y = (-2,1,2,-1)

    def func(x,y,cnt) :
        global result
        if 0<=x<N and 0<=y<N and not(visited[y][x]):
            cnt+=1
            visited[y][x]=1

            if cnt == N :
                result =1

            for i in range(4) :
                nx = x + move_x[i]
                ny = y + move_y[i]
                if 0 <= nx < N and 0 <= ny < N :
                    func(nx,ny, cnt)

    cnt = 0
    for y in range(N) :
        for x in range(N) :
            result=0
            visited=[[0]*N for _ in range(N)]
            func(x,y,0)
            if result :
                cnt+=1



    
    print("#{} {}".format(tc, cnt))

