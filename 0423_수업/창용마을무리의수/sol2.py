import sys
sys.stdin = open("input.txt")

T = int(input())

def find_set(x) :
    while parent[x] != x : # 대표 원소를 찾을 때 까지
        x= parent[x]
    return x

def union(x, y) :
    parent[find_set(y)] = find_set(x)

for tc in range(1, T+1):
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]

    for _ in range(M) :
        x, y = map(int, input().split())
        union(x,y)

    result = 0
    for i in range(1, N+1) :
        if parent[i] == i :
            result+=1

    print("#{} {}".format(tc, result))

