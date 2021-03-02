import sys
sys.stdin = open("input.txt")

T = 10

icp = { # 넣을 때
    '+' : 1,
    '*' : 2,
    '-' : 1,
    "/" : 2,
    "(" : 3
}
isp = { # 스택안
    '+' : 1,
    '*' : 2,
    '-' : 1,
    "/" : 2,
    "(" : 0
}

def to_back(inp) : # 후위 연산식으로 바꾸기
    N = len(inp)
    result = [0] * N
    stack =[]

    j=0 # result 인덱스
    for tmp in inp :
        if tmp.isdigit() : # 숫자일 경우
            result[j] = tmp
            j+=1
        else: # 연산자일 경우

            if not stack :# 스택이 비어있는 경우
                stack.append(tmp)
                continue

            else : # 스택이 비어있지 않은 경우
                # 닫는 괄호일 경우, 여는 괄호가 나올 때까지 pop
                if tmp == ')' :
                    while stack[-1] != '(' :
                        result[j] = stack.pop()
                        j+=1
                    stack.pop() # '(' 제거

                # 연산 우선순위 비교
                elif icp[tmp] > isp[stack[-1]] : # 넣는 연산자가 stack 맨뒤 연산자보다 우선순위가 높을 경우
                    stack.append(tmp)

                else : # 넣는 연산자가 stack 맨뒤 연산자보다 우선순위가 낮은 경우
                    while icp[tmp] <= isp[stack[-1]] : # 넣는 연산자가 stack 맨뒤 연산자보다 우선순위가 높아질때까지 연산
                        result[j] = stack.pop()
                        j+=1
                    stack.append(tmp)

    result = filter(lambda x : x != 0, result) # 괄호가 사라지면서 인덱스 줄어들음, 0들 제거
    return result

def calc(back_equ) :
    result = 0
    stack = []
    for tmp in back_equ :
        if tmp.isdigit() : # 숫자면
            stack.append(tmp)
        else : # 연산식이면
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if tmp == "+" :
                tmp_result = num1+num2
            elif tmp == "*" :
                tmp_result = num1*num2
            elif tmp=="-" :
                tmp_result = num1-num2
            elif tmp=="/" :
                tmp_result = num1 // num2 # 나누어떨어진다는 가정

            stack.append(tmp_result)

    return stack[0]


for tc in range(1, T+1):
    N= int(input())
    inp = input()

    back_equ = to_back(inp)
    result = calc(back_equ)

    print("#{} {}".format(tc, result))

