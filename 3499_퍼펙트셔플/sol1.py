import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = input().split()
    L = len(inp_arr)

    half = (len(inp_arr)+1) //2

    print("#{}".format(tc), end="")

    for i in range(half) :
        if i<half :
            print(" {}".format(inp_arr[i]), end="")
        if i+half<L :
            print(" {}".format(inp_arr[i+half]), end="")

    print()



