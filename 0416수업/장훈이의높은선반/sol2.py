import sys
sys.stdin = open("input.txt")

T = int(input())

def func() :
    s = set()
    s.add(0)
    min_result = 10000*N
    for tmp in inp_arr :
        s2 = set()
        for tmp2 in s :
            tmp_result = tmp+tmp2
            if tmp_result>B :
                if min_result > tmp_result :
                    min_result = tmp_result
            elif tmp_result == B :
                return B
            else :
                s2.add(tmp_result)
        s= s.union(s2)
    return min_result

for tc in range(1, T+1):
    N, B = map(int, input().split())
    inp_arr = list(map(int, input().split()))
    result = func()-B

    
    print("#{} {}".format(tc, result))

