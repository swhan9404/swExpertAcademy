T = int(input())

def get_parent(x) : #부모찾기
    while x != parent_arr[x] :
        x = parent_arr[x]
    return x

def func(start, end, val) : # 최소비용트리
    global result
    if result > M :
        return

    if get_parent(start) != get_parent(end) :
        parent_arr[get_parent(start)] = end
        result+=val

def dijkstra(x) : # 다익스트라
    visited[x] = 1
    val_arr[x] = 0
    cnt = 1 # 모든 점을 다 방문하고 종료하기 위한 cnt

    while cnt <= V :
        for i in range(1, V+1) :
            if map_arr[x][i] != 0 and not visited[i] and map_arr[x][i]+val_arr[x] < val_arr[i] :
                val_arr[i] = map_arr[x][i]+val_arr[x]

        next = 0
        for i in range(1, V+1) :
            if not visited[i] and val_arr[i] < val_arr[next] :
                next = i
        x = next
        cnt+=1


for tc in range(1, T+1):
    V, E, M = map(int, input().split())
    # V : 도시갯수
    # E : 도로 갯수
    # M : 건설 예산
    inp_arr = [list(map(int, input().split())) for _ in range(E)] # 도로 / 도로 / 비용
    inp_arr.sort(key=lambda x: x[2])
    parent_arr = [i for i in range(V+1)]
    result = 0

    for road in inp_arr :
        func(*road)

    if result > M :
        val_arr = [9876543210] * (V+1) # 1에서 나머지 점들을 가는 비용
        map_arr = [[0] * (V+1) for _ in range(V+1)] # map_arr[start][end] = 비용
        visited = [0] * (V+1) # 방문했는지 체크
        for road in inp_arr : # map_arr 만들기
            start, end, val = road
            map_arr[start][end] = val
            map_arr[end][start] = val

        dijkstra(1)
        answer = M- val_arr[V] 

    else :
        answer = M- result

    print("#{} {}".format(tc, answer))

