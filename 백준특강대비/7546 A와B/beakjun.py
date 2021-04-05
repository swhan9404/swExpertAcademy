# https://www.acmicpc.net/problem/12904
# DFS - 시간초과
# DFS + 종료조건 추가 하면 풀릴거같은데

S = input()
T = input()

result = False
def func(S, T) :
    global result
    reverse_S = S[::-1]
    if len(S) == len(T) :
        if S == T :
            result = True
        return

    if not result :
        func(S+'A', T)
    if not result :
        func(reverse_S+'B', T)

func(S,T)
if result :
    print(1)
else:
    print(0)