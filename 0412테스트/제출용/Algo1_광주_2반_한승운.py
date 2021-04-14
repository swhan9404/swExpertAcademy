import sys
sys.stdin = open("문제1_input.txt")

T = int(input())

move_x = [1,1,-1,-1] # 1시 / 5시 / 7시 / 11시
move_y = [-1,1,1,-1]
def func(y, x, power) :
    cnt= 0
    for tmp_power in range(0, power+1) : #크기
        for i in range(4) : # 방향
            tmp_x = x + tmp_power * move_x[i]
            tmp_y = y + tmp_power * move_y[i]

            if 0<=tmp_x<N and 0<=tmp_y<N :
                cnt += inp_arr[tmp_y][tmp_x] # 적군 수
                inp_arr[tmp_y][tmp_x] =0 # 폭발 한 곳 적군 수 초기화
    return cnt


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 지도의 크기
    # M : 폭탄의 수

    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    boom_arr = [list(map(int, input().split())) for _ in range(M)]
    # 위치_y / 위치_x / 세기

    result =0
    for tmp_boom in boom_arr :
        result+=func(*tmp_boom)

    print("#{} {}".format(tc, result))

