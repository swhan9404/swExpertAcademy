import sys
sys.stdin = open("input.txt")

T = int(input())


def count_color() : # 줄별 색깔 갯수
    white = [0] * N
    blue = [0] * N
    red = [0] * N

    for y in range(N):
        for x in range(M) :
            tmp = inp_arr[y][x]
            if tmp == "R" :
                red[y] +=1
            elif tmp == "B" :
                blue[y] +=1
            else :
                white[y]+=1
    return white, blue, red

def func() : # b,r 시작위치 ( w는 0 고정)

    result = N * M  # 나올 수 있는 최대 경우의 수로 초기화
    white, blue, red = count_color()  # 색깔 별 줄당 색깔 갯수

    for b in range(1, N-1) :
        for r in range(b+1, N) :
            tmp_result =0
            for w_line in range(0,b) : # 흰색 바꾸기
                tmp_result+= M-white[w_line]
                if tmp_result > result :
                    break
            for b_line in range(b, r) : # 파란색 바꾸기
                tmp_result += M - blue[b_line]
                if tmp_result > result :
                    break
            for r_line in range(r, N) : # 빨간색 바꾸기
                tmp_result+= M - red[r_line]
                if tmp_result > result :
                    break

            if result > tmp_result :
                result = tmp_result

    return result


for tc in range(1, T+1):
    # N : 줄
    # M : 문자갯수
    N, M = map(int, input().split())
    inp_arr = [input() for _ in range(N)]

    result = func()

    print("#{} {}".format(tc, result))

