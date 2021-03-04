import sys
sys.stdin = open("input.txt")

from collections import deque
T = int(input())

def func(start) :
    queue = deque([(start, 0)])
    visited = [0] * (V+1) # 인덱스 맞추기 위해 앞에 한칸 비우기
    while queue : # 큐가 빌때까지
        now, distance = queue.popleft()
        if now == G : # 도착하면 거리 반환
            return distance
        elif visited[now] == 0 : # 방문하지 않았다면
            visited[now]=1
            distance+=1
            for next in dic[now] :
                queue.append([next, distance])


for tc in range(1, T+1):
    # V : 노드의 개수
    # E : 간선 정보
    V, E  = map(int, input().split())
    dic = {}
    for _ in range(E) :
        start, end = map(int, input().split())

        tmp = dic.get(start, list())
        tmp.append(end)
        dic[start] = tmp

        tmp =dic.get(end, list())
        tmp.append(start)
        dic[end] = tmp

    # S : 출발노드
    # G : 도착노드
    S, G = map(int, input().split())
    result = func(S)
    if result == None :
        result =0

    print("#{} {}".format(tc, result))

