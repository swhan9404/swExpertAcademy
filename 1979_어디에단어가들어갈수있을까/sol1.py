import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 퍼즐 크기
    # K : 단어의 길이
    N, K = map(int, input().split())
    inp_arr = [0] * N
    for i in range(N) :
        inp_arr[i] = list(map(int, input().split()))

    move_x = [1,-1,0,0] # 오른쪽 왼쪽 위 아래
    move_y = [0,0,-1,1] #

    result = 0
    for y in range(N) :
        for x in range(N) :
            if inp_arr[y][x] == 1 :
                garo = 1 # 가로길이
                sero = 1 # 세로 길이

                for i in range(4) : # 움직이면서 가로세로 길이 구하기
                    dx =x
                    dy= y
                    while True :
                        dx += move_x[i]
                        dy += move_y[i]
                        if not (0 <= dx < N) or not(0<=dy<N) or inp_arr[dy][dx] != 1:
                            break

                        if i in [0,1] : # 가로 길이체크일때
                            garo += 1
                        else : # 세로 길이 체크일때
                            sero +=1

                # 길이 체크 후 count
                if garo == K :
                    result+=1
                if sero == K :
                    result+=1

    # 길이만큼 중복되게 세어졌기 때문에 나눠주기
    result//=K

    print("#{} {}".format(tc, result))

