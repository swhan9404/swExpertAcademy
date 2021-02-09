import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N 번 정류장까지 이동
    # K : 한번 이동시 최대 이동할수 있는 정류장수
    # M : 충전지가 설치된 M개의 정류장 갯수
    # sta_arr : 충전지가 설치된 정류장 리스트
    # result : 충전한 위치 리스트
    K, N, M = map(int,input().split())
    sta_arr = list(map(int, input().split()))

    sta_arr.append(N) # 마지막 위치도 충전 위치로 취급시키기
    fuel = K # 현재 남은 연료
    result= []

    for i in range(1, N+1) :
        fuel -=1

        # 현재 위치에 충전기가 있으면
        if i in sta_arr :
            check = False

            # 연료 다 쓸 때까지 다음 충전기가 있는지 확인
            for j in range(i+1, i+1+fuel) :
                if j in sta_arr :
                    check = True
            # 충전기가 있으면
            if check :
                continue
            # 충전기가 없으면 충전하기
            else :
                result.append(i)
                fuel = K
        # 연료가 떨어져서 목적지까지 갈 수 없을 경우
        if fuel == 0 :
            result =[]
            break

    # 도착 위치에서 충전을 했으면 빼주기
    if N in result :
        result.remove(N)
    print("#{} {}".format(tc, len(result)))

