import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # P : A사의 1리터 가격
    # Q : B사의 가격 (R리터 이하)
    # R : B사의 가격기준
    # S : B사의 가격(R리터 초과)
    # W : 수도의 양
    P, Q, R, S, W = map(int, input().split())

    result_A = P*W
    result_B = Q # 기본요금
    if W > R :
        result_B += S*(W-R) # 초과분에 대한 가격

    result = min(result_A, result_B)
    print("#{} {}".format(tc, result))

