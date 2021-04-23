import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input()) # 섬의 갯수
    island_arr= [list(map(int, input().split())) for _ in range(N)]
    E = float(input()) # 세율

    print("#{} ".format(tc, ))

