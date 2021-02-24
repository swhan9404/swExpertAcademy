import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input()) # 카드 갯수
    inp_arr = list(map(int, input().split()))

    result = 0 #최대 길이
    joker_cnt = 0
    for tmp in inp_arr :
        if tmp == 0 :
            joker_cnt +=1
    for _ in range(joker_cnt) : inp_arr.remove(0) # 리스트에서 0 제거
    sort_arr = sorted(inp_arr) # 정렬하기

    for i in range(len(sort_arr)) :
        joker_chance = joker_cnt
        k = 1 # 인덱스
        j = 1 # 길이
        start = sort_arr[i]
        while i+k<len(sort_arr) :
            if sort_arr[i+k] != start+j :
                if joker_chance != 0 : #조커 찬스가 남아있을 경우
                    joker_chance-=1
                    j +=1
                    continue
                else :
                    break
            k += 1
            j += 1
        if j > result :
            result = j


    
    print("#{} {}".format(tc, result))

