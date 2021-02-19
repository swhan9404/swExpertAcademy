import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp_arr = [0] * 5
    max_len = 0
    for i in range(5) :
        inp = input()
        inp_arr[i] = inp
        if max_len < len(inp) :
            max_len = len(inp)

    print("#{} ".format(tc), end="")
    for x in range(max_len) :
        for y in range(5) :
            try :
                print(inp_arr[y][x], end="")
            except :
                continue
    print()



