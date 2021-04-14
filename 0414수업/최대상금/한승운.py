import sys
sys.stdin = open("input.txt")

T = int(input())

# greedy 로 풀시 틀림
"""
32888 2 의 경우
> 82883 -> 88823 이 되는데 실제로는 88832 가 되어야함
"""


def func(number, N) :
    cnt = 0

    for i in range(0, len(number)) :
        tmp_standard = number[i]
        tmp_max, tmp_idx = 0, 0
        for j in range(i+1, len(number)) :
            if tmp_max <= number[j] :
                tmp_max = number[j]
                tmp_idx = j
        else :
            if tmp_standard < tmp_max :
                number[i], number[tmp_idx] = number[tmp_idx], number[i]
                cnt+=1
        if cnt == N :
            return number

    while cnt < N :
        number[len(number)-1], number[len(number)-2] = number[len(number)-2], number[len(number)-1]
        cnt+=1
    return number

for tc in range(1, T+1):
    number, N = input().split()
    N = int(N)
    number = list(map(int, list(number)))

    result = map(str,func(number, N))


    print("#{} {}".format(tc, ''.join(result)))

