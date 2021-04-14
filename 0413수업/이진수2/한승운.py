import sys
sys.stdin = open("input.txt")

T = int(input())

def func(N) :
    cnt = 0
    result_list = []
    while cnt <13 :
        cnt+=1
        N*=2
        if int(N) == 1 :
            N-= 1
            result_list.append('1')
        else :
            result_list.append('0')
        if N == 0 :
            break
    else :
        return 'overflow'
    return ''.join(result_list)

for tc in range(1, T+1):
    N = float(input())
    result = func(N)
    
    print("#{} {}".format(tc, result))

