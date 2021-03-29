import sys
sys.stdin = open("input.txt")

T = int(input())

def find_start() :
    tmp_max = 0
    return_list = []
    for y in range(N) :
        for x in range(N) :
            if inp_arr[y][x] > tmp_max :
                tmp_max = inp_arr[y][x]
                return_list.clear()
                return_list.append((x,y))
            elif inp_arr[y][x] == tmp_max :
                return_list.append((x, y))
    return tmp_max, return_list

move_x = (1,-1,0,0)#오른쪽, 왼쪽, 위, 아래
move_y = (0,0,-1,1)

def DFS(start_x, start_y, depth, before_val, use) : #시작점, 현재 깊이, 이전값, 구멍팠는지
    global max_length
    # 방문했거나,
    now_val = inp_arr[start_y][start_x]

    if now_val>= before_val : # 크기가 이전꺼보다 작거나(구멍도 이미 한번 팠으면) 끝
        if use == True : # 이미 구멍파기 사용
            return
        else : # 구멍파기 사용하기
            dig = now_val -  before_val + 1 # 얼마나 파야할지
            if dig <= K : # K보다 파야할게 작아서 팔 수 있으면
                use = True
                now_val = before_val -1
            else :
                return

    if max_length < depth : # 최대길이 비교
        max_length = depth

    for i in range(4) :
        dx = start_x + move_x[i]
        dy = start_y + move_y[i]

        if (0<= dx < N) and (0<= dy < N) and visited[dy][dx]!=1 :
            visited[dy][dx] =1
            DFS(dx, dy, depth+1, now_val, use)
            visited[dy][dx] = 0


for tc in range(1, T+1):
    N, K = map(int, input().split())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    visited= [[0] * N for _ in range(N)]
    max_length= 0

    max_value, max_list = find_start()
    for start_x, start_y in max_list :
        visited[start_y][start_x] = 1
        DFS(start_x, start_y, 1, 21, False)
        visited[start_y][start_x] = 0


    print("#{} {}".format(tc, max_length))

