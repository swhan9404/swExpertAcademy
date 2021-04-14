import sys
sys.stdin = open("input.txt")

T = int(input())


def convert(x) : # 10진법을 2진법으로 변환
    tmp_list = [0] * 4
    for i in range(3, -1, -1) :
        x, tmp_list[i] = divmod(x,2)
    return ''.join(map(str,tmp_list))

def make_table(dic) :
    table = {x : convert(dic[x]) for x in dic}
    return table

for tc in range(1, T+1):
    N, bit_16 = input().split()
    dic1 = { str(x) : x for x in range(10)}
    dic2 =  {chr(x) : x-ord('A')+10 for x in range(ord('A'),ord('F')+1)}
    dic = {**dic1, **dic2} # 16 > 10 진법 변환 테이블 만들기

    table = make_table(dic) # 16 진법 > 2진법 변환 테이블
    result_list = [table[x] for x in bit_16]


    print("#{} {}".format(tc, ''.join(result_list)))

