import sys
sys.stdin = open("input.txt")

# 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다 => permutation 실제 계산량 10! > 가능
T = int(input())

def func(N) : # 지금 바꿀 찬스가 몇번 남았는지
    global result
    if N == 0 :
        tmp = int(''.join(number))
        if result < tmp :
            result = tmp
        return

    for i in range(length) :
        for j in range(i+1, length) :
            number[i], number[j] = number[j], number[i]
            tmp = ''.join(number)
            if visited.get((tmp, N-1), True) : # N 단계에서 방문을 하지 않았다면 True 반환 // 이거 안하면 중복때매 너무 오래걸림
                visited[(tmp, N-1)] = False
                func(N-1)
            number[i], number[j] = number[j], number[i]


for tc in range(1, T+1):
    number, N = input().split()
    N = int(N)
    number = list(number)
    length = len(number)
    visited = {}
    result = 0
    func(N)

    print("#{} {}".format(tc, result))

