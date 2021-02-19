import sys
sys.stdin = open("input.txt")


def func():
    for y in range(N):
        for x in range(N):
            if inp_arr[y][x] == 'o':
                cnt = 1
                for dx, dy in move:
                    for j in range(1, 5):
                        if 0 <= x + dx * j < N and 0 <= y + dy * j < N and inp_arr[y + dy * j][x + dx * j] == 'o':
                            cnt += 1
                        else:
                            break
                    else:
                        return 'YES'

    return 'NO'


move = ((1, 0), (0, 1), (1, 1), (-1, 1))  # 가로, 세로, 대각오, 대각왼
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    inp_arr = [input() for _ in range(N)]
    result = func()

    print('#{} {}'.format(tc, result))

