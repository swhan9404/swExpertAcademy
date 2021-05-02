import sys
sys.stdin = open("문제1_input.txt")

T = int(input())

def check(cnt_arr) : # 베이비진 체크
    result_cnt = 0

    for i in range(10) : # 동일카드 3개 체크
        if cnt_arr[i] >=3 :
            cnt_arr[i] -= 3
            result_cnt +=1

    for i in range(0, 8) : # 연속카드 체크
        if cnt_arr[i]>=1 and cnt_arr[i+1]>=1 and cnt_arr[i+2]>=1 : # 연속된 수 이면
            min_cnt = min(cnt_arr[i], cnt_arr[i+1], cnt_arr[i+2]) # 1 1 2 2 3 3 같은거 들어올때를 위해 min
            cnt_arr[i] -=min_cnt
            cnt_arr[i+1] -= min_cnt
            cnt_arr[i+2] -= min_cnt
            result_cnt +=min_cnt

    return result_cnt


for tc in range(1, T+1):
    inp = input()
    cnt_arr = [0] * 10

    for word in inp :
        cnt_arr[int(word)] +=1

    result = check(cnt_arr)
    if result == 2 :
        answer = 1
    else :
        answer = 0

    print("#{} {}".format(tc, answer))

