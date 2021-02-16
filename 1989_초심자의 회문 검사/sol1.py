import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    result = 1 if inp == inp[::-1] else 0

    print("#{} {}".format(tc, result))

