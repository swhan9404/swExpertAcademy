import sys
sys.stdin = open("input.txt")
# youtube 교수님 코드 내가 정제한 것

T = int(input())

for tc in range(1, T+1):
    inp_arr = list(map(int,list(input()))) # Baby Gin 확인할 6자리 수
    cnt_arr = [0]* 10 # 6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트

    for tmp in inp_arr :
        cnt_arr[tmp] +=1

    i = 0 # 횟수 세기
    tri = run =0 # tri, run 변수 초기화

    while i < 10 :
        if cnt_arr[i] >= 3 : # triplet 조사후 데이터 삭제
            cnt_arr[i] -= 3
            tri +=1
            continue
        if i <= 7 :
            if cnt_arr[i] >=1 and cnt_arr[i+1] >=1 and cnt_arr[i+2] >=1 : #run 조사후 데이터 삭제
                cnt_arr[i] -=1
                cnt_arr[i+1] -=1
                cnt_arr[i+2] -=1
                run +=1
                continue
        i+=1

    if run + tri == 2 :
        result = 1
    else :
        result =0

    print("#{} {}".format(tc, result))
