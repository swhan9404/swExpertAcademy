# https://www.acmicpc.net/problem/16953
start, end = map(int, input().split())

INF = 999999999
min_cnt = INF

def func(x, y, cnt) :
    global min_cnt
    if x == y :
        if cnt < min_cnt :
            min_cnt = cnt
        return
    elif x > y :
        return

    #1
    func(2 * x, y, cnt+1)
    #2
    func(10*x+1, y, cnt+1)

func(start, end, 1)
if min_cnt == INF:
    print("-1")
else :
    print(min_cnt)