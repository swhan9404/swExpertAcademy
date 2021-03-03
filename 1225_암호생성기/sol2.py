import sys
sys.stdin = open("input.txt")

T = 10

# list 구현 = 143 ms 실행시간
for tc in range(1, T+1):
    nothing = input()
    inp_arr = list(map(int, input().split()))

    i = 0
    while True:
        front = inp_arr.pop(0)  # 맨 앞 값 뺴오기
        front -= (i % 5) + 1  # 순서만큼 빼주기
        if front <= 0:
            front = 0
            inp_arr.append(front)
            break
        inp_arr.append(front)  # 다시 넣기
        i += 1  # 순서 증가

    result = " ".join(map(str, inp_arr))

    print("#{} {}".format(tc, result))

