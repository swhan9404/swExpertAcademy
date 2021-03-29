import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # D : 하루 요금
    # M : 한달 요금
    # T : 3달 요금
    # Y : 1년 요금
    D, M, T, Y = map(int, input().split())
    inp_arr = list(map(int, input().split()))
    cost_list = [0] *12

    for i in range(12) :
        before = cost_list[i-1] if i-1>=0 else 0

        day_cost = (D * inp_arr[i] )+before
        month_cost = M +before

        t_day_cost = 0
        month_cost = 3 * M
        for j in range(3) :
            t_day_cost+= inp_arr[i+j] * D


    print("#{} {}".format(tc, cost_list[-1]))

