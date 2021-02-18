import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 글자판 크기
    # M : 원하는 회문 길이
    N, M = map(int, input().split())
    inp_arr = [input() for _ in range(N)]

    result = ""
    # 가로 체크
    def garo() :
        for y in range(N) :
            for x in range(N-M+1) :
                for i in range(M//2) : # 절반만 체크(회문이니까)
                    if inp_arr[y][x+i] != inp_arr[y][x+M-1-i] :
                        break
                else : # 전부 통과가 된다면
                    return inp_arr[y][x:x+M]
    # 세로 체크
    def sero() :
        for x in range(N) :
            for y in range(N-M+1) :
                for i in range(M//2) : # 절반만 체크(회문이니까)
                    if inp_arr[y+i][x] != inp_arr[y+M-1-i][x] :
                        break
                else : # 전부 통과가 된다면
                    tmp_result = ""
                    for dy in range(y,y+M) :
                        tmp_result+= inp_arr[dy][x]
                    return tmp_result
    result = garo()
    if not result :
        result = sero()

    print("#{} {}".format(tc, result))

