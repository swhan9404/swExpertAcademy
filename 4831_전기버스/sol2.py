import sys
sys.stdin = open("input.txt")

T = int(input())

# 일단 최대로 가보고 (만약에 종점 이상이면 그냥 break)
# 그 위치부터 하나씩 빼면서 충전기를 만나는 위치로 이동
# 만약에 충전기가 없이 시작 위치로 돌아오게 된다면
# 0 으로 출력하기

for tc in range(1, T+1):
    # N 번 정류장까지 이동
    # K : 한번 이동시 최대 이동할수 있는 정류장수
    # M : 충전지가 설치된 M개의 정류장 갯수
    # sta_arr : 충전지가 설치된 정류장 리스트
    K, N, M = map(int, input().split())
    sta_arr = list(map(int, input().split()))

    point = 0 # 움직이기 전 위치
    move = 0 # 움직이고 나서 위치
    result = 0 # 몇번 충전했는지

    while point < N:

        for i in range(point+K, point, -1) :
            if i >= N or i in sta_arr:
                move = i
                break
        if move == point :
            result =0
            break
        else :
            result +=1
            point = move

    print("#{} {}".format(tc, max(0,result-1)))

