import sys
sys.stdin = open("input.txt")

""" input.txt
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

T = int(input())

def DFS(start) :
    stack = [start]
    while stack :
        tmp_start= stack.pop()
        if visited[tmp_start] :
            continue
        visited[tmp_start] = 1
        print(tmp_start, end=" ")
        for i in range(N, -1, -1) :
            if map_arr[tmp_start][i] and not visited[i] :
                stack.append(i)

def BFS(start) :
    queue= [start]
    visited[start] =1
    while queue :
        queue2 = []
        for point in queue :
            print(point, end=" ")
            for i in range(N+1) :
                if map_arr[point][i] and not visited[i]:
                    queue2.append(i)
                    visited[i] = 1
        queue= queue2


for tc in range(1, T+1):
    N, V = map(int, input().split())
    inp_arr = list(map(int, input().split()))
    map_arr = [[0]*(N+1) for _ in range(N+1)]
    visited=[0] * (N+1)

    for i in range(0, len(inp_arr), 2) :
        start= inp_arr[i]
        end= inp_arr[i+1]

        map_arr[start][end] = 1
        map_arr[end][start] = 1

    #BFS(1)
    #DFS(1)

    #print("#{} ".format(tc, ))

