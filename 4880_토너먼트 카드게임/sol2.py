import sys
sys.stdin = open("input.txt")

T = int(input())

def win(x,y) : # 누가 이겼는지
    first = inp_arr[x]
    second = inp_arr[y]
    if (first-second+3)% 3 == 2 : # y의 승리
        return y
    else : # x 승리, 비김
        return x

def func(start, end) : # 두그룹으로 나누기
    if start == end :
        return start

    first = func(start, (start+end)//2)
    second = func((start+end)//2+1, end)
    return win(first, second)

for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))
    result = func(0, N-1)
    result+=1 # 인덱스 맞춰주기
    
    print("#{} {}".format(tc, result))

