import sys
sys.stdin = open("input.txt")

T = int(input())

def route(x, parent_arr) : # 해당 점을 route에서 부터 가는 루트 구하기
    route_arr = []
    now_x = x
    while now_x != 0 :
        route_arr.append(now_x)
        now_x = parent_arr[now_x]
    route_arr.reverse()
    return route_arr

def tree_size(x, child_arr) : # 밑에 길이 구하기
    size = 0
    queue = [x]
    while queue :
        queue2 = []
        for tmp in queue :
            queue2.extend(child_arr[tmp])
        size+= len(queue)
        queue = queue2
    return size


for tc in range(1, T+1):

    V, E, N1, N2 = map(int, input().split())
    inp_arr = list(map(int,input().split()))
    parent_arr = [0] * (V+1)
    child_arr = [[] for _ in range(V+1)]
    for i in range(0,len(inp_arr),2) :
        parent_arr[inp_arr[i+1]] = inp_arr[i] # 해당 점을 route에서 부터 가는 길 구하기 용
        child_arr[inp_arr[i]].append(inp_arr[i+1]) # 밑에 길이 구하기 용

    route_N1 = route(N1, parent_arr)
    route_N2 = route(N2, parent_arr)
    result = 0

    for i in range(len(route_N1)) : # 루트 부터 N1, N2 로 가는 길을 순서대로 따라가면서 분기되는 순간 끝남
        if route_N1[i] != route_N2[i] :
            result = route_N1[i-1]
            break

    
    print("#{} {} {}".format(tc, result, tree_size(result, child_arr)))

