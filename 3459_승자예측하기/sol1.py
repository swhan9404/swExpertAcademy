import sys
sys.stdin = open("input.txt")

T = int(input())

# 어려웟음

for tc in range(1, T+1):
    N= int(input())

    minus = 1
    cnt =0

    # 규칙성
    # 1 4 4 16 16
    while N > 0 :
        N -= minus
        if not (cnt % 2) : # 짝수일때만
            minus *=4
        cnt +=1  # 횟수


    if cnt % 2 : # 홀수
        result= "Bob"
    else :
        result="Alice"
    print("#{} {}".format(tc, result))

