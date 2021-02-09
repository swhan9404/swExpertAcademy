import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    # Test_len : 테스트 케이스 길이
    # Test_case
    # result : 조망권이 확보된 갯수
    Test_len = int(input())
    Test_case = list(map(int, input().split()))
    result =0

    # 해당 건물의 조망권 체크
    def view_check(i) : # 몇번째 건물인지
        height = Test_case[i]

        max_height = 0 # 좌우 2칸까지 건물들의 최대 높이
        for tmp in Test_case[i-2:i] + Test_case[i+1: i+3] :
            if tmp > max_height :
                max_height= tmp

        # 건물 높이 - 최대 높이 = 조망권 확보된 갯수
        diff = height - max_height

        # 음수일수도 있기 때문에 else로 0 처리
        return diff if diff >0 else 0

    for i in range(2, Test_len-2) : # 양옆 2칸은 공백
        result += view_check(i)

    print("#{} {}".format(tc, result))

