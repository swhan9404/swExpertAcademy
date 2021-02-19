import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    inp_arr = ["".join(input().split()) for _ in range(N)]

    def func1(i) : # 출력 첫요소 ↑방향 → 이동
        result = ""
        for y in range(N-1, -1, -1) :
            result+=inp_arr[y][i]
        return result

    def func2(i) : # 출력 두번째 요소 ←방향 ↑이동
        result = ""
        for x in range(N-1,-1,-1) :
            result +=inp_arr[N-i-1][x]
        return result

    def func3(i) : # 출력 세번째 요소 ↓방향 ←이동
        result = ""
        for y in range(N) :
            result += inp_arr[y][N-i-1]
        return result


    print("#{}".format(tc))
    for i in range(N) :
        print("{} {} {}".format(func1(i),func2(i),func3(i)))



