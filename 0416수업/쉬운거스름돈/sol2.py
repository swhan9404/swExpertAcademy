import sys
sys.stdin = open("input.txt")

T = int(input())

money = [50000,10000,5000,1000,500,100,50,10]

for tc in range(1, T+1):
    inp = int(input())
    count_arr = [0] * len(money)

    for i in range(len(money)) :
        count_arr[i], inp = divmod(inp, money[i])

    
    print("#{}".format(tc))
    print(*count_arr)

