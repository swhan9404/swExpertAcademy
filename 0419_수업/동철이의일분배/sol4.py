import sys
sys.stdin = open("input.txt")

for t in range(int(input())):
    n = int(input())
    m = 1<<n
    d = [0]*m
    p = [[*map(lambda x:x/100,map(int,input().split()))] for _ in range(n)]
    d[0] = 1
    for mask in range(m):
        x = sum(1 for i in range(n) if mask&(1<<i))
        for j in range(n):
            if mask&(1<<j) == 0:
                d[mask|(1<<j)] = max(d[mask|(1<<j)],d[mask]*p[x][j])
    print(f'#{t+1} {d[-1]*100:.6f}')
