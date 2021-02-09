import sys
sys.stdin = open("input.txt")
# youtube 교수님 코드

T = int(input())


for tc in range(1, T+1):
    num = int(input()) # Baby Gin 확인할 6자리 수
    c = [0]* 12 # 6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트 ( 하단에 i+2 때문에 11자리까지 생성)

    for i in range(6) :
        c[num % 10] += 1
        num //=10

    i = 0
    tri = run =0

    while i < 10 :
        if c[i] >= 3 : # triplet 조사후 데이터 삭제
            c[i] -= 3
            tri +=1
            continue
        if c[i] >=1 and c[i+1] >=1 and c[i+2] >=1 : #run 조사후 데이터 삭제
            c[i] -=1
            c[i+1] -=1
            c[i+2] -=1
            run +=1
            continue
        i+=1

    if run + tri == 2 :
        result = 1
    else :
        result =0

    print("#{} {}".format(tc, result))
