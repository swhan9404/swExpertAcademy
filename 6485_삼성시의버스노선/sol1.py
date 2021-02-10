import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 버스 노선 갯수
    # i 번째 버스 노선 : A[i] 이상 B[i] 이하
    # P_arr : 정류장 리스트
    # result : 각 정류장마다 버스노선이 몇개 다니는지 적은 리스트

    N = int(input())
    A_arr = [0] * (N+1) # 첫자리는 비어잇음 주의
    B_arr = [0] * (N+1) # 첫자리는 비어잇음 주의

    for i in range(1, N+1) :
        a, b = map(int, input().split())
        A_arr[i] = a
        B_arr[i] = b

    # 버스마다 노선 튜플로 정리한 리스트
    bus_arr = list(zip(A_arr, B_arr))

    P = int(input())
    C_arr = [0] * P
    for i in range(P) :
        C_arr[i] = int(input())

    result = [0] * P
    for i in range(P) :
        for j in range(len(bus_arr)) :
            if bus_arr[j][0] <= C_arr[i] <= bus_arr[j][1] :
                result[i] +=1

    result = map(str, result)
    result = " ".join(result)
    print("#{} {}".format(tc, result))

