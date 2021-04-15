import sys
sys.stdin = open("input.txt")

T = int(input())


def check(deck) :
    for i in range(10) :
        if deck[i] == 3 :
            return True

    check = 0
    for i in range(10) :
        if deck[i] :
            check +=1

        else :
            check = 0

        if check == 3:
            return True
    return False

for tc in range(1, T+1):
    inp_arr = list(map(int, input().split()))
    first = [0] * 10
    second = [0] * 10

    result = 0 # 0 이면 무승부 / 1 이면 first 승 / 2이면 second 승
    for i in range(len(inp_arr)) :
        if i%2 :
            second[inp_arr[i]] +=1
            if check(second) :
                result = 2
                break
        else :
            first[inp_arr[i]] +=1
            if check(first) :
                result = 1
                break
    
    print("#{} {}".format(tc, result))

