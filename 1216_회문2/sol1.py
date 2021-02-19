import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    tc = int(input())

    N = 100
    inp_arr = [input() for _ in range(N)]

    result = 1 # 최고 회문 길이

    # 가로 회문 판단
    for y in range(N) :
        for x in range(N) :
            for end in range(N, x+result, -1) : # 뒤에서 부터 확인(있다면 그 이하 길이는 판단안해도됨, 그리고 result보다 작은길이도 판단할필요없음)
                for d in range( (end-x) //2 ) :
                    if inp_arr[y][x+d] != inp_arr[y][end-1-d] :
                        break
                else :
                    tmp = end-x
                    if tmp > result :
                        result = tmp

    #세로 회문 판단
    for x in range(N) :
        for y in range(N) :
            for end in range(N, y + result, -1):
                for d in range( (end-y) //2 ) :
                    if inp_arr[y+d][x] != inp_arr[end-1-d][x] :
                        break
                else :
                    tmp = end-y
                    if tmp > result :
                        result = tmp

    print("#{} {}".format(tc, result))

