import sys
sys.stdin = open("input.txt")

T = 10

dic = {
    '+' : 1,
    '*' : 2,
    '-' : 1,
    "/" : 2,
}

for tc in range(1, T+1):
    N = int(input())
    inp = input()

    # 후위 표현식 만들기
    def func(inp) :
        back_cal = [0] * N

        j=0 # back_cal 인덱스용
        stack = []
        for i in range(N) :
            tmp = inp[i]
            if tmp in dic.keys() : # 연산자이면
                if stack : # 스택이 비어있지 않으면
                    now_priority = dic[tmp]
                    before_priority = dic[stack[-1]]
                    if now_priority >= before_priority : # 현재 우선순위 >= 이전연산자 우선순위
                        stack.append(tmp)
                    else : # 아니라면 stack 비우기
                        while stack :
                            back_cal[j] = stack.pop()
                            j+=1
                else : # 스택이 비어있다면
                    stack.append(tmp)

            else : # 숫자이면
                back_cal[j] = int(tmp)
                j+=1

        while stack:
            back_cal[j] = stack.pop()
            j += 1

        return back_cal

    def func2(inp) :
        stack = []
        for tmp in inp :
            if tmp in dic.keys() : # 연산자이면
                two = stack.pop()
                one = stack.pop()
                if tmp == "+" :
                    result = one+two
                elif tmp == "*" :
                    result = one*two
                elif tmp == "/":
                    result = one/two
                elif tmp == "-" :
                    result = one-two
                print(result)
                stack.append(result)
            else: #숫자면
                stack.append(tmp)
        return stack.pop()

    back_cal= func(inp)
    result = func2(back_cal)
    
    print("#{} {}".format(tc, result))

