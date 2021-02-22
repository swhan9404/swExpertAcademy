T = int(input())


for tc in range(1, T+1):
    start = input()
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    result = start # 누가 이겼는지 저장
    A_where = B_where = 0 # A, B 말의 위치
    turn = 0 # 몇턴째인지 ( 원래 턴 보다 -1)

    def check(who) : # who를 기준으로 두 말이 같은 위치에 있으면 who가 다른걸 잡아먹음
        global A_where, B_where
        if A_where == B_where :
            if who == "A" :
                B_where =0
            else :
                A_where =0
        return

    def check_win() : # 승부가 났는지 체크 및 결과입력
        global result
        if A_where >= 20 :
            result = "A"
            return True
        elif B_where >= 20 :
            result="B"
            return True

        return False


    for i in range(10) :

        if start == "A" :
            A_where += A_arr[i]
            check("A")
            if check_win() : # A가 20을 넘은경우 끝냄
                break

            B_where += B_arr[i]
            check("B")
            if check_win() : # B가 20을 넘은경우 끝냄
                break

        else : # start가 B인 경우
            B_where += B_arr[i]
            check("B")
            if check_win():  # B가 20을 넘은경우 끝냄
                break

            A_where += A_arr[i]
            check("A")
            if check_win():  # A가 20을 넘은경우 끝냄
                break
    else : # 승부가 안난 경우 무승부
        result = "AB"

    print("#{} {}".format(tc, result))

