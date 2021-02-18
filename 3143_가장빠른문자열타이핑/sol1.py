import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    A, B = input().split()

    i = 0
    result = 0
    while i < len(A) :
        if i<len(A)-len(B)+1 and A[i:i+len(B)] == B :
            i += len(B) -1
        i += 1
        result +=1
    print("#{} {}".format(tc, result))

