import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    dic = {
        "(" : ")",
        "{" : "}"
    }
    stack = []
    result =1

    for tmp in inp :
        if tmp in dic.keys() : # "(", "{" 면 스택에추가
            stack.append(tmp)
        elif tmp in dic.values() :
            if len(stack) : # 스택이 비어있지 않으면 pop
                if tmp != dic[stack.pop()] : # 짝이 맞지 않는 경우
                    result =0
                    break
            else : # 스택이 비어있는데 pop할 경우는 break
                result =0
                break

    if stack : #스택이 비어있지 않으면
        result =0

    print("#{} {}".format(tc, result))

