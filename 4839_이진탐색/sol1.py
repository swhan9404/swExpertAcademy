import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # P : 책 페이지 수
    # A : A가 찾을 페이지
    # B : B가 찾을 페이지
    P, A, B = map(int, input().split())
    result_A = result_B = result = 0

    def func(start_x, end_x, find_page, cnt) :
        c = (start_x+end_x) //2
        cnt += 1
        result=0
        # 페이지가 c와 같으면 끝내기
        if c == find_page :
            return cnt

        if c > find_page : # 왼쪽탐색
            result= func(start_x, c, find_page, cnt)
        elif c < find_page : # 오른쪽 탐색
            result =func(c, end_x, find_page, cnt)
        return result

    result_A = func(1, P, A, 0)
    result_B = func(1, P, B, 0)

    # 결과
    if result_A < result_B : # A승리
        result= "A"
    elif result_A > result_B :# B승리
        result = "B"
    else : # 비김
        result = "0"
    print("#{} {}".format(tc, result))

