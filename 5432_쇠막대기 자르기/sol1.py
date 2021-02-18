import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    cnt = 0
    result =0
    back=")"
    for tmp in inp :
        if tmp == "(" :
            cnt+=1
        else :
            cnt -= 1
            if back=="(" :
                result += cnt  # 잘리는 판의 갯수
            else :
                result+=1 # 판이 끝날때 남는 조각 1개

        back=tmp #이전꺼

    print("#{} {}".format(tc, result))

