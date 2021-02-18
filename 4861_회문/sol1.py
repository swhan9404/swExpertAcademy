import sys
sys.stdin = open("input.txt")

T = int(input())

# 실패한것
for tc in range(1, T+1):
    # N : 글자판 크기
    # M : 원하는 회문 길이
    N, M = map(int, input().split())
    inp_arr = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    def func(x, y) : #판단 위치
        if (not(0<=x<N-M+1) and not(0<=y<N-M+1)) or visited[y][x]: # 바깥으로 나감, 방문했음
            return

        result =""
        visited[y][x] = 1
        # 가로 확인
        if 0<=x<N-M+1 :
            for dx in range(M//2) :
                if inp_arr[y][x+dx] != inp_arr[y][x+M-1-dx] :
                    break
            else :
                result = inp_arr[y][x:x+M]
                return result

        # 세로 확인
        if 0<=y<N-M+1 :
            for dy in range(M//2) :
                if inp_arr[y+dy][x] != inp_arr[dy+M-1-dy][x] :
                    break
            else :
                for dy in range(y,y+M) :
                    result += inp_arr[dy][x]
                return result

        # 아니면 오른쪽, 아래로 기준점 움직이기
        result =func(x+1,y)
        if result :
            return result
        result = func(x,y+1)
        if result :
            return result

    result = func(0,0)
    print("#{} {}".format(tc, result))

