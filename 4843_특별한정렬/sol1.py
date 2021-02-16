import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    end = N if N<10 else 10 # 어디까지 출력할지

    for i in range(end) :
        if i % 2 : # 홀수번쨰
            min = inp_arr[i]
            min_idx = i
            for j in range(i, N) :
                if min > inp_arr[j] :
                    min_idx = j
                    min = inp_arr[j]
            inp_arr[i] , inp_arr[min_idx] = inp_arr[min_idx], inp_arr[i]
        else : # 짝수번째
            max = inp_arr[i]
            max_idx = i
            for j in range(i, N) :
                if max < inp_arr[j] :
                    max_idx = j
                    max = inp_arr[j]
            inp_arr[i] , inp_arr[max_idx] = inp_arr[max_idx], inp_arr[i]


    print("#{} ".format(tc) , end="")
    print(*inp_arr[:end], sep=" ")

