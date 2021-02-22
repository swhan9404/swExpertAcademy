## 왜 틀렸지??

K = int(input())

large_height = 0 # 큰 높이
large_height_d = 0 # 큰 높이 인덱스

large_width = 0 # 큰 너비
large_width_d = 0 # 큰 너비 인덱스

inp_arr =[list(map(int, input().split())) for _ in range(6)]

# 큰 높이, 너비
for i in range(6) :
    direction, length = inp_arr[i]

    if direction in [1,2] : #동쪽, 서쪽
        if large_width < length :
            large_width = length
            large_width_d = i
    else :
        if large_height < length :
            large_height = length
            large_height_d = i

# 큰 사각형 크기
result1 = large_height * large_width

# 뺄 사각형
cut =[large_height_d+1, large_height_d, large_height_d-1]+[large_width_d+1, large_width_d, large_width_d-1]   # 큰높이 주변 선분 인덱스+큰너비

#주변 선분 인덱스
for i in range(len(cut)) :
    if cut[i] <0 :
        cut[i] = 6+cut[i]

result2 = 1
for i in range(6) :
    if i not in cut :
        result2 *= inp_arr[i][1] # 해당 인덱스 길이 추출

print((result1-result2)*K)

