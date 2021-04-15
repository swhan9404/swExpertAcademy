import sys
sys.stdin = open("input.txt")

T = int(input())

def cost(tour) : # 가는방법을 통해 비용검사
    tmp_sum = 0
    now = 0
    for end in tour+[0] :
        tmp_cost = inp_arr[now][end]
        if tmp_cost == 0 :
            return INF
        else :
            tmp_sum += tmp_cost
        now = end
    return tmp_sum

def swap(k) : # 어디까지 섞었는지
    global result
    if k ==  len(tour)-1:
        tmp_sum = cost(tour)
        if result > tmp_sum :
            result = tmp_sum

    for j in range(k, len(tour)) :
        tour[k], tour[j] = tour[j], tour[k]
        swap(k+1)
        tour[k], tour[j] = tour[j], tour[k]


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [list(map(int, input().split())) for _ in range(N)]
    tour = list(range(1,N)) # 2~ N 문제에써져있는건데 저는 여기서 0부터시작
    INF = 100 * N
    result = INF
    swap(0)

    print("#{} {}".format(tc, result))
0.12283s
