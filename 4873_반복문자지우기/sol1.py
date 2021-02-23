import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    stack = list(inp) # 만들기

    def func(stack) :
        for i in range(len(stack)-1) :
            end = len(stack) # 반복 글자 끝 위치값 초기화
            if stack[i] == stack[i+1] :
                return func(stack[:i]+stack[i+2:])
        else :
            return stack

    result = func(stack)
    print("#{} {}".format(tc, len(result)))

