import sys
sys.stdin = open("input.txt")

T = int(input())

# 스택을 이용한 풀이
for tc in range(1, T+1):
    inp = input()
    stack = []
    result = 0
    back = 0

    for tmp in inp :
        if tmp == "(" :
            stack.append(tmp)
        else :
            stack.pop()
            if back != tmp :
                result += len(stack) # 쌓여있는 판 갯수
            else :
                result +=1

        back = tmp
    print("#{} {}".format(tc, result))

