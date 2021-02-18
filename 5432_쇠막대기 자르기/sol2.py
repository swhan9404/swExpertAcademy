import sys
sys.stdin = open("input.txt")

T = int(input())
# 제한 시간 초과

for tc in range(1, T+1):
    inp = input()
    L = len(inp)

    cnt_close = 0 # () 괄호가 닫혔는지 체크
    cnt = 0 # 안에 () 가 몇개 들었는지 체크
    result = 0 # 결과

    for i in range(L) :
        cnt = 0
        cnt_close = 0
        if inp[i] == "(" :
            cnt_close +=1
            for j in range(i+1, L) : # 그 다음부터 끝까지 확인 - 괄호 닫히는 거 체크
                if inp[j] == "(" :
                    cnt_close +=1
                    if j < L-1 and inp[j+1] == ")" : # () 괄호 갯수세기
                        cnt+=1
                else :
                    cnt_close -=1
                    if cnt_close == 0 :
                        result += cnt+1 if cnt!=0 else 0 # cnt 가 0이 아니면 cnt+1 로 더해지고, 아니면 0
                        break


    print("#{} {}".format(tc, result))

