# https://www.acmicpc.net/problem/12907

N = int(input())
inp_arr = list(map(int, input().split()))

def func(inp_arr) :
    tmp_len = len(inp_arr)
    for i in range(N//2 + 1) :
        tmp_cnt = inp_arr.count(i)
        tmp_len -= tmp_cnt
        if tmp_cnt == 2 :
            continue
        elif tmp_cnt == 1 :
            if tmp_len == 0 :
                return i + 1
            else :
                tmp_inp_arr = [x for x in inp_arr if x >= i]
                if func2(tmp_inp_arr, i) :
                    return i if i >0 else 1
                return 0
        else :
            if tmp_len == 0 :
                return i
            else :
                return 0

def func2(inp_arr, i) :
    if inp_arr == list(range(i, i+len(inp_arr))):
        return 1
    return 0

tmp = func(inp_arr)
result = 2 ** tmp
if result == 1 :
    print(0)
else :
    print(result)