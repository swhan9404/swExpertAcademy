import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    def func(arr) :
        print(*arr, sep=" ")
        if len(arr)== N :
            return

        result = [0] * (len(arr) + 1)
        for i in range(len(result)) :
            if 0<= i < len(arr) :
                tmp1 = arr[i]
            else :
                tmp1 = 0
            
            if 0<= i-1 < len(arr) :
                tmp2 = arr[i-1]
            else :
                tmp2 = 0

            result[i] =tmp1 +tmp2
        func(result)
    
    print("#{} ".format(tc ))
    func([1])


