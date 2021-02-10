import sys
sys.stdin = open("input.txt")
# Youtube 풀이 - 해당 높이에 대한 블럭 세기 (나의 풀이와 동일한데 살짝 다름) - 가장 진화된 버전
# 에러남 확인할것
T = 10
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] *101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자
    for i in range(100) :
        h_cnt[box[i]] += 1
        if box[i] > max_value :
            max_value = box[i]
        if box[i] < min_value :
            min_value = box[i]

    while N > 0 and min_value < (max_value -1) :
        # 상자 옮기기
        box[min_value] -=1
        box[min_value +1] +=1

        box[max_value] -=1
        box[max_value - 1] +=1

        #포인터를 변경하자
        if box[min_value] == 0:
            min_value +=1
        if box[max_value] == 0 :
            max_value -=1

        # 덤프 줄이기
        N -=1

    print("#{} {}".format(tc, max_value - min_value))

