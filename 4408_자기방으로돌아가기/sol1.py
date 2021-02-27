import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input()) # 학생수

    dup_visit = [0] * 201
    for i in range(N) :
        start, end = map(int, input().split())

        # start 가 항상 end보다 작게 만들어주기
        if start > end :
            start, end = end, start

        def func(x) : # (1,2) =1 , (3,4)=2 이렇게들을 같은 수들로 묶어주기 위함
            if x % 2 : # 홀수
                return (x+1)//2
            else : # 짝수
                return x//2

        start = func(start)
        end = func(end)

        # 구간이 몇번 반복되었는지를 위해 구간 cnt
        for j in range(start, end+1) :
            dup_visit[j] +=1

    # 가장 많이 반복된 구간의 반복회수 구하기
    max_dup = 0
    for i in range(len(dup_visit)) :
        if dup_visit[i] > max_dup :
            max_dup = dup_visit[i]

    print("#{} {}".format(tc, max_dup))

