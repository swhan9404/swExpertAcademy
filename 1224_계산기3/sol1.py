import sys
sys.stdin = open("input.txt")
T = 10
ISP = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
ICP = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}


def getPostfix(user_str):
    stack = []
    result = ''
    for c in user_str:
        # 연산자
        if c in ISP.keys():
            if not stack:
                stack.append(c)
            else:
                while ISP[stack[-1]] >= ICP[c]:
                    result += stack.pop()

                stack.append(c)
        # 피연산자
        else:
            if c == ')':
                while True:
                    now = stack.pop()
                    if now == '(':
                        break
                    result += now

            else:
                result += c

    while stack:
        result += stack.pop()

    return result


def calByPostfix(postfix):
    stack = []
    for c in postfix:
        if c in ISP.keys():
            second = stack.pop()
            first = stack.pop()
            if c == '*':
                stack.append(first * second)
            else:
                stack.append(first + second)
        else:
            stack.append(int(c))

    return stack.pop()


for tc in range(1, T + 1):
    N = int(input())
    infix = input()
    postfix = getPostfix(infix)
    result = calByPostfix(postfix)
    print("#{} {}".format(tc, result))


