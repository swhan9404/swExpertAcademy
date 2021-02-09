import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 카드 장수
    inp_arr = list(map(int, list(input()))) # 입력 카드들

    cnt_arr = [0] *10 # 몇장인지 세는 거 (0~9)

    for tmp in inp_arr :
        cnt_arr[tmp] +=1

    max_val =0
    max_idx =0

    for i in range(10) : # (0~9) 자리를 각각 돌면서
        if cnt_arr[i] >= max_val : # 카드 장수가 같을 때 큰 쪽을 출력할수 있도록 = 까지 추가
            max_val = cnt_arr[i]
            max_idx = i


    print("#{} {} {}".format(tc, max_idx, max_val))

