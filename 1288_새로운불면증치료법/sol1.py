import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N= int(input())

    result_arr = set()
    result_cnt=0
    while len(result_arr)<10:
        inp = N* (result_cnt+1)

        while inp>0 :
            result_arr.add(inp%10)
            inp//=10

        result_cnt+=1

    result = N* (result_cnt)
    print("#{} {}".format(tc, result))

