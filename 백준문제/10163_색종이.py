# https://www.acmicpc.net/problem/10163
N = int(input()) # N장 종이

inp_arr = [list(map(int, input().split())) for _ in range(N)]

pan = [[0]*101 for _ in range(101)] # 판 만들고

for i in range(N) : # 판에 종이 깔고
    x,y,w,h = inp_arr[i]

    pan_num = i+1
    for height in range(h) :
        for width in range(w) :
            pan[y+height][x+width] = pan_num

for i in range(1,N+1) : # 판 넓이 재고
    result= 0
    for y in range(101) :
        result+=pan[y].count(i)
    print(result)