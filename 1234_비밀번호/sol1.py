import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    N, inp_arr = input().split()
    N= int(N)

    stack = [inp_arr[0]]
    for i in range(1, len(inp_arr)) :
        if stack and inp_arr[i] == stack[-1] : # 스택이 비어있지 않고 스택 맨 위값이 지금 넣는 값과 같을 때
            stack.pop()
        else :
            stack.append(inp_arr[i])
    
    print("#{} {}".format(tc, "".join(stack)))

