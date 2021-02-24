import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr=[list(map(int, input().split())) for _ in range(N)]

    y_list= []
    for y in range(N) :
        tmp = sum(inp_arr[y])
        if tmp % 2 : # 홀수면
            y_list.append(y)

    x_list= []
    for x in range(N) :
        tmp = 0
        for y in range(N) :
            tmp+=inp_arr[y][x]

        if tmp % 2 : # 홀수면
            x_list.append(x)

    result = ""
    if len(x_list)==0 and len(y_list) ==0 :
        result = "OK"
    elif len(x_list)==1 and len(y_list) ==1 :
        result = "Change bit ({},{})".format(y_list[0]+1,x_list[0]+1) # 1부터 시작이라 1씩 더해주기
    else :
        result = "Corrupt"

    print("#{} {}".format(tc, result))

