import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp_arr = input().split()

    stack = []
    for tmp in inp_arr :
        if tmp.isdigit() : # 숫자라면
            stack.append(int(tmp))
        elif tmp =="." :
            if len(stack) == 1 :
                result = stack.pop()
            else :
                result = "error"
            break
        else : # 수식이라면
            if len(stack) < 2 :
                result = "error"
                break
            second = stack.pop()
            first = stack.pop()

            if tmp == "+" :
                result = first + second
            elif tmp == "*" :
                result = first * second
            elif tmp == "/" :
                result = first // second # 나누어 떨어지기 때문에
            else :
                result = first - second

            stack.append(result)
    
    print("#{} {}".format(tc, result))

