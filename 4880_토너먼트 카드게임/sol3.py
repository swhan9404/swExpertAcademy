import sys
sys.stdin = open("input.txt")

T = int(input())

# sol1 부전승 부분 고친것
for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    def func(arr) : # 매개 -누구랑 누구가 뜨는지 인덱스 리스트
        print(arr)
        if len(arr) ==1 :
            return arr[0]

        next_arr = [0] * ((len(arr)+1)//2) # 새로운 승자 인덱스 리스트
        i = 0 # arr idx
        j = 0 # next_arr idx
        while i<len(arr) :
            front = inp_arr[ arr[i] ]
            if len(arr)%2==1 and i==len(arr)//2 :
                next_arr[j] = front
                j+=1
                i+=1
                continue
            if i+1<len(arr) :
                end = inp_arr[ arr[i+1] ]
            else :
                next_arr[j] = front
                j += 1
                i += 2
                continue


            result = (front-end +3 ) %3 # 0 :비김 1 :front승  2:end승
            if result ==0 :
                next_arr[j] = arr[i] # 비기면 번호가 작은 애가 이김
            elif result == 1: # front 승
                next_arr[j] = arr[i]
            else : # end 승
                next_arr[j] = arr[i+1]

            i+=2
            j+=1

        return func(next_arr)

    result = func(range(N))
    result +=1 # 인덱스 맞춰주기( 문제에서는 1부터 시작하므로)

    print("#{} {}".format(tc, result))

