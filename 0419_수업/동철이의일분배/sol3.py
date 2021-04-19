import sys
sys.stdin = open("input.txt")

def norm(a):
    return int(a)/100
 
def dfs(depth, prob):
    global n, answer
    if prob <= answer:
        return
    if depth == n:
        answer = max(answer, prob)
        return
    for i in range(n):
        if not v[i]:
            v[i] = True
            dfs(depth + 1, prob * p[depth][i])
            v[i] = False
 
for t in range(int(input())):
    n = int(input())
    p = [list(map(norm, input().split())) for _ in range(n)]
    v = [False] * n
    answer = 0
    dfs(0, 100)
    print("#{} {:.6f}".format(t+1, answer))