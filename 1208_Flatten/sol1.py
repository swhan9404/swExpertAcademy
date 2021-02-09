import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    dump_n = int(input()) # 덤핑 횟수 제한
    box_height = list(map(int, input().split())) # 상자들의 높이

    height_cnt = [0] * 101 # 0~ 100 까지 각 층별 블럭 갯수
    for height in box_height :
        for i in range(height+1) :
            height_cnt[i] +=1

    max_h = 100
    min_h = 0
    while dump_n >0 :
        dump_n -= 1
        for i in range(max_h, -1, -1) :
            if height_cnt[i] : # 높이에 대한 갯수가 0이 아니면
                height_cnt[i]-=1
                max_h = i
                break # for문에 대한 break

        for i in range(min_h, 101) :
            if height_cnt[i] != 100 :
                height_cnt[i] +=1
                min_h = i
                break # for문에 대한 break

        #print(max_h, min_h)
        if max_h - min_h <2 :
            break

    # 그 칸수가 100인 최대 높이
    for i in range(100) :
        if height_cnt[i] == 100 :
            min_h = i
        else :
            break

    # 칸수가 0 이 아닌 최대 높이
    for i in range(100, -1, -1) :
        if height_cnt[i] != 0 :
            max_h = i
            break

    # for i in range(10) :
    #     print(i,"번째" ,height_cnt[(i)*10: (i+1)*10])
    # print(max_h, min_h)
    print("#{} {}".format(tc, max_h-min_h))

