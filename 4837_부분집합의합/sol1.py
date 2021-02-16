import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    A = list(range(1,13)) # 1~12 집합
    # N 개의 원소
    # K : 부분집합의 합
    N, K = map(int, input().split())
    result = 0

    for i in range(1<<len(A)) :
        tmp_arr = []
        for j in range(len(A)) :
            if i & (1<<j) :
                tmp_arr.append(A[j])

        if len(tmp_arr) == N and sum(tmp_arr) == K :
            result+=1

    
    print("#{} {}".format(tc, result))

