import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    result = 0
    check = "0" # 이전꺼
    for tmp in inp :
        if check != tmp : # 이전에 바꾼거랑 달라졌으면
            result+=1
            check=tmp
    
    print("#{} {}".format(tc, result))

