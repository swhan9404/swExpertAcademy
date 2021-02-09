import sys
sys.stdin = open("input.txt")

# 테스트 케이스가 하나 안통과함(runtime error)
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    inp_arr = list(map(int, input().split()))

    # 90도 로 떨어졌을 때 나오는 결과
    result_arr = [0] * N
    for tmp in inp_arr :
        for i in range(tmp) :
            result_arr[i] += 1

    # 결과로 낙차를 계산해서 최대 낙차 구하기
    result = 0
    for i in range(N) :
        for j in range(inp_arr[i] if inp_arr[i]<=N else N) :
            tmp = (N-i)-result_arr[j]
            if tmp> result :
                result = tmp

    print("#{} {}".format(tc, result))

