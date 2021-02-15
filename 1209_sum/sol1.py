import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    # 가로
    for y in range(100) :
        sum =0
        for x in range(100) :
            sum+=arr[y][x]

        if result < sum :
            result = sum

    # 세로
    for x in range(100) :
        sum=0
        for y in range(100) :
            sum+=arr[y][x]

        if result<sum :
            result = sum

    # 대각선 ( 오른쪽 아래)
    sum =0
    for x in range(100) :
        sum+=arr[x][x]

    if result < sum :
        result = sum

    # 대각선 오른쪽 위
    sum=0
    for x in range(100) :
        sum+= arr[x][(100-1)-x]
    if result < sum :
        result = sum

    print("#{} {}".format(tc, result))

