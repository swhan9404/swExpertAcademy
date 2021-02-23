import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    def func(arr) : #재귀용도
        print(*arr, sep=" ")
        if len(arr)== N :
            return

        result = [0] * (len(arr) + 1)

        for i in range(len(result)) : # 길이가 n 되면 끝내기
            if 0<= i < len(arr) : # 오류처리로 인덱스 에러나는 양끝값 0으로 처리
                tmp1 = arr[i]
            else :
                tmp1 = 0
            
            if 0<= i-1 < len(arr) :
                tmp2 = arr[i-1]
            else :
                tmp2 = 0

            result[i] =tmp1 +tmp2 # 규칙성적용
        func(result)
    
    print("#{} ".format(tc ))
    func([1])


