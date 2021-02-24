import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):

    N = int(input())
    inp = input()

    # 후위 계산식으로 만들기
    back_cal = [0] * N
    stack = []
    i = 0
    for tmp in inp :
        if ord("0") <= ord(tmp) <= ord("9") :
            back_cal[i] = tmp
            i+=1
            if stack :
                back_cal[i] = stack.pop()
                i+=1
        else :
            stack.append(tmp)

    # 후위표기법 연산
    stack2 = []
    for tmp in back_cal :
        if ord("0") <= ord(tmp) <= ord("9") :
            stack2.append(tmp)
        else : # 연산자
            back = stack2.pop()
            front = stack2.pop()
            if tmp == "+" :
                result = int(front) + int(back)
                stack2.append(str(result))

    print("#{} {}".format(tc, stack2.pop()))

