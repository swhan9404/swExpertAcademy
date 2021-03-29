import sys
sys.stdin = open("input.txt")

T = int(input())

# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWo3QBrKSewDFAQi&categoryId=AWo3QBrKSewDFAQi&categoryType=CODE
for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    inp_arr.sort()
    for i in range(1,N) :
        inp_arr[i] = inp_arr[i]+inp_arr[i-1]

    print("#{} {}".format(tc, sum(inp_arr)))

