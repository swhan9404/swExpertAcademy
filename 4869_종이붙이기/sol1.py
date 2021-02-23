import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    N //= 10 # 편의성을 위해 N을 10 나누고 시작

    result_arr = [0] * N
    try : # 혹시 N이 0이나 1이 들어올 경우를 대비
        result_arr[0] = 1
        result_arr[1] = 3
    except :
        pass

    for i in range(2, N) : # 피보나치 처럼 생각
        result_arr[i] = 2* (result_arr[i-2]) + result_arr[i-1]
        # 아이디어 앞에 1 하나를 두고 하는 경우의 수 = result_arr[i-2]
        # 아이디어 앞에 2 하나를 두고 하는 경우의 수 = (2를 만드는 방법 =2개 (3개에서 11 하나 제외) ) * result_arr[i-1]

    print("#{} {}".format(tc, result_arr[N-1]))

