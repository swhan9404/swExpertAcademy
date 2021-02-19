import sys
sys.stdin = open("input.txt")

T = int(input())


def func():
    # 가로
    for y in range(N):
        check = [1] + [0] * 9
        for x in range(N):
            check[inp_arr[y][x]]+=1
        if 0 in check :
            return 0

    # 세로
    for x in range(N):
        check = [1] + [0] * 9
        for y in range(N):
            check[inp_arr[y][x]] += 1
        if 0 in check  :
            return 0

    # 3x3
    for y in range(0,N,3) :
        for x in range(0,N,3) :
            # 여기부터 해당 3x3
            check = [1] + [0] * 9
            for dy in range(3) :
                for dx in range(3) :
                    check[inp_arr[y+dy][x+dx]] += 1
            if 0 in check:
                return 0
    return 1

for tc in range(1, T+1):
    N= 9
    inp_arr = [list(map(int,input().split())) for _ in range(9)]

    check = [1]+[0] * 9 # 맨앞 0 햇갈리니 제거

    result = func()
    print("#{} {}".format(tc, result))

