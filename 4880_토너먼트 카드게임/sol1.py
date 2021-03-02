import sys
sys.stdin = open("input.txt")

T = int(input())

# 왠지모르겠는데 10개중 4개 테스트 케이스 통과
for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))

    def func(arr) : # 매개 -누구랑 누구가 뜨는지 인덱스 리스트

        if len(arr) ==1 :
            return arr[0]

        next_arr = [0] * ((len(arr)+1)//2) # 새로운 승자 인덱스 리스트
        for i in range(0,len(arr),2) :
            front = inp_arr[ arr[i] ]
            try :
                end = inp_arr[ arr[i+1] ]
            except : # 만약 마지막에 대결할 상대가 없을경우

                next_arr[i//2] = arr[i]
                continue

            result = (front-end +3 ) %3 # 0 :비김 1 :front승  2:end승
            if result ==0 :
                next_arr[i//2] = arr[i] # 비기면 번호가 작은 애가 이김
            elif result == 1: # front 승
                next_arr[i//2] = arr[i]
            else : # end 승
                next_arr[i//2] = arr[i+1]

        return func(next_arr)

    result = func(range(N))
    result +=1 # 인덱스 맞춰주기( 문제에서는 1부터 시작하므로)

    print("#{} {}".format(tc, result))

