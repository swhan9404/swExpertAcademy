import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 두 기차 전면부의 거리
    # A : A기차 속력
    # B : B기차 속력
    # F : 파리의 속력
    D, A, B, F = map(int, input().split())

    time = D / (A+B) # 파리의 이동시간
    result = time * F # 파리속력 * 이동시간
    
    print("#{} {}".format(tc, result))

