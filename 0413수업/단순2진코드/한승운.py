import sys
sys.stdin = open("input.txt")

T = int(input())

def func(x) : # 검증코드
    even_sum = 0
    odd_sum = 0
    cnt = True # 짝수면 True 홀수면 False

    while x :
        cnt = False if cnt else True
        x, y = divmod(x, 10)
        if cnt :
            even_sum += y
        else :
            odd_sum += y

    cal_code = (even_sum*3 + odd_sum)% 10

    if cal_code == 0 :
        return even_sum + odd_sum
    else :
        return 0

def find_line(inp_arr, M) : #옳바른 데이터 찾아서 반환
    for line in inp_arr :
        for i in range(M-1, (56 -1 -1), -1) :
            if line[i] == '1' :
                return line[i+1-56 :i+1]

def convert(inp_arr, M) : # 옳바른 데이터를 받아서 result로 converting
    data = find_line(inp_arr, M)
    result = 0
    for i in range(8) :
        start = i*7
        cut_data = data[start:start+7]
        real_data = dic[cut_data]
        result += real_data * 10 ** (7-i)
    return result


for tc in range(1, T+1):
    N, M = map(int, input().split())
    inp_arr = [input() for _ in range(N)]

    dic = {
        "0001101" : 0,
        "0011001" : 1,
        "0010011" : 2,
        "0111101" : 3,
        "0100011" : 4,
        "0110001" : 5,
        "0101111" : 6,
        "0111011" : 7,
        "0110111" : 8,
        "0001011" : 9
    }

    convert_data = convert(inp_arr, M)
    result = func(convert_data)

    print("#{} {}".format(tc, result))

