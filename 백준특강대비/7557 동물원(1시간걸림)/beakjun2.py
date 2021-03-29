N = int(input())
inp_arr = list(map(int, input().split()))


def func(inp_arr) :
    cnt_arr = [0] * 40
    for i in range(40) :
        cnt_arr[i] = inp_arr.count(i)
    return cnt_arr
cnt_arr = func(inp_arr)

def func2(cnt_arr) :
    cnt = 0
    alpha = 0
    for i in range(40) :
        if cnt_arr[i] == 2:
            cnt+=1
            if alpha : # alpha == 1
                return 0
        elif cnt_arr[i] == 1:
            alpha=1
            continue
        elif cnt_arr[i] == 0 :
            if sum(cnt_arr[i+1:]) != 0 :
                return 0
            else :
                return cnt+alpha
        else :
            return 0
    return cnt+alpha
tmp = func2(cnt_arr)
result  = 2 ** tmp
if result == 1 :
    print(0)
else :
    print(result)