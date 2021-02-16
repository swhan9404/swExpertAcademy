import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    result = [[0] *10 for _ in range(10)] # 10x10 격자

    N = int(input()) # 점 갯수
    inp_arr = [0] * N
    for i in range(N) : # 입력받기
        inp_arr[i]=(list(map(int, input().split())))

    for i in range(N) :
        r1,c1,r2,c2,color = inp_arr[i]

        for y in range(r1, r2+1) :
            for x in range(c1, c2+1) :
                point = result[y][x]

                if point == 0 :
                    result[y][x] = color
                elif point != color : # 서로 다른색
                    result[y][x] = 3
                else : #같은색
                    pass

    result_cnt = 0
    for y in range(10) :
        for x in range(10) :
            if result[y][x] == 3 :
                result_cnt+=1

    print("#{} {}".format(tc, result_cnt))

