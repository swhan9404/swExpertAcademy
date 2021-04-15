import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [ list(map(int, input().split())) for _ in range(N)]

    inp_arr.sort(key=lambda x : x[1]) # 끝나는 순으로 정렬시키기

    result = 0
    tmp_end = 0
    for time in inp_arr :
        if tmp_end <= time[0] :
            tmp_end = time[1]
            result+=1

    print("#{} {}".format(tc, result))

