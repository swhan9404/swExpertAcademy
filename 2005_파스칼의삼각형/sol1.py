import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = input()

    def func(arr) :

        if len(arr)== N :
            return

        result = [0] * (len(arr) + 1)
        for i in range(len(result)) :
            try :
                tmp1 = arr[i]
            except :
                tmp2 = arr[i+1]

            result[i] =
    
    print("#{} ".format(tc, ))

