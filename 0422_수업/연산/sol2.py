import sys
sys.stdin = open("input.txt")

T = int(input())

def BFS(N, M) :
    queue = [N]
    cnt = 0
    while queue :
        queue2 = []
        for now in queue :
            if now == M :
                return cnt
            next = now +1
            if 0<=next<1000001 and not visited[next] :
                queue2.append(next)
                visited[next] = 1
            next = now - 1
            if 0 <= next < 1000001 and not visited[next]:
                queue2.append(next)
                visited[next] = 1
            next = now * 2
            if 0 <= next < 1000001 and not visited[next]:
                queue2.append(next)
                visited[next] = 1
            next = now - 10
            if 0 <= next < 1000001 and not visited[next]:
                queue2.append(next)
                visited[next] = 1
        queue = queue2
        cnt += 1
    return


for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001 # 갔던 곳 다시 안가게
    result = BFS(N, M)
    print("#{} {}".format(tc, result))

