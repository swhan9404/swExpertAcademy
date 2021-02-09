import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    inp_arr = list(map(int, list(input())))
    all_case = []
    tmp_case = [0] * len(inp_arr)
    isSelected = [0] * len(inp_arr)

    # 케이스 만들어서 돌리기
    def make_case(n):
        if n == len(inp_arr):
            if check(tmp_case):
                if tmp_case not in all_case:  # 이 조건은 사실 없어도됨
                    all_case.append(list(tmp_case))
            return

        for i in range(len(inp_arr)):
            if not isSelected[i]:
                tmp_case[n] = inp_arr[i]
                isSelected[i] = 1
                make_case(n + 1)
                isSelected[i] = 0

    # 케이스 확인
    def check(inp_arr):
        check1 = False
        check2 = False

        if inp_arr[0] == inp_arr[1] and inp_arr[1] == inp_arr[2]:
            check1 = True

        if inp_arr[3] == inp_arr[4] and inp_arr[4] == inp_arr[5]:
            check2 = True

        if inp_arr[0] + 1 == inp_arr[1] and inp_arr[1] + 1 == inp_arr[2]:
            check1 = True

        if inp_arr[3] + 1 == inp_arr[4] and inp_arr[4] + 1 == inp_arr[5]:
            check2 = True

        return check1 and check2

    make_case(0)
    # print(all_case)
    result = 1 if all_case else 0
    print("#{} {}".format(tc, result))

