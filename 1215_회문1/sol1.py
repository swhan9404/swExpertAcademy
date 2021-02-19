import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):

    K = int(input()) # 찾아야하는 회문길이
    inp_arr = [input() for _ in range(8)]

    def garo(x, y) :
        cnt = 0
        # 가로 판별
        for i in range(K//2) :
            if inp_arr[y][x+i] != inp_arr[y][x+(K-1)-i] :
                break
        else :
            return 1
        return 0

    def sero(x,y) :
        # 세로 판별
        for i in range(K//2) :
            if inp_arr[y+i][x] != inp_arr[y+(K-1)-i][x] :
                break
        else :
            return 1
        return 0

    result =0
    # 가로판별
    for y in range(8) :
        for x in range(8-K+1) :
            result+= garo(x,y)
    #세로 판별
    for x in range(8) :
        for y in range(8-K+1) :
            result+=sero(x,y)


    print("#{} {}".format(tc, result))

