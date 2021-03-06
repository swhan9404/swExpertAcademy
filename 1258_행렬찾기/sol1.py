import sys
sys.stdin = open("input.txt")

T = int(input())

def find() : # 부분 시작 확인
    for y in range(N):
        for x in range(N) :
            if inp_arr[y][x] != 0 :
                return x, y

def find_area(start_x, start_y) : # 범위 확인/ 매개변수 :시작위치
    end_y = N # 마지막점 포함x
    end_x = N # 마지막점 포함x

    for tmp_y in range(start_y, N) : # 끝위치 찾기
        if inp_arr[tmp_y][start_x] == 0 :
            end_y = tmp_y
            break

    for tmp_x in range(start_x, N) : # 끝 위치 찾기
        if inp_arr[start_y][tmp_x] == 0 :
            end_x = tmp_x
            break

    return end_x, end_y

def visited(start_x, start_y, end_x, end_y) : # 범위 찾은곳 제거
    for y in range(start_y, end_y) :
        for x in range(start_x, end_x) :
            inp_arr[y][x] = 0
    return


for tc in range(1, T+1):
    N = int(input())
    inp_arr = [ list(map(int, input().split())) for _ in range(N)]
    result = []# 부분행렬의 (행과열) 크기 리스트

    while find() :
        start_x, start_y = find() # 안칠한 부분의 시작점 (맨왼쪽 위에 점 찾기)
        end_x, end_y = find_area(start_x, start_y)  # 안칠한 부분 맨 아래점 ( 맨 오른쪽, 맨 아래쪽 점 찾기)

        length_x = end_x - start_x
        length_y = end_y - start_y
        result.append( (length_y, length_x) ) # result 에 행길이, 열길이 튜플로 넣기
        visited(start_x, start_y, end_x, end_y) # 지금 체크한 영역 초기화

    result = sorted(result, key = lambda rectangle : (rectangle[0]*rectangle[1],rectangle[0])) # 넓이 정렬

    print("#{} {} ".format(tc, len(result)), end="")
    for tmp in result :
        print(*tmp, end=" ")
    print()

