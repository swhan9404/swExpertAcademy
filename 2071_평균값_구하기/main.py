import sys
# stdin = standard input 표준입력
sys.stdin = open('input.txt') # input 파일 불러옴

T = int(input())
for i in range(1,T+1) :
    inp_arr = list(map(int, input().split()))

    # sum, len 안쓰기
    sum_ =0
    len_ =0
    for tmp in inp_arr :
        sum_+=tmp
        len_+=1
    result = sum_ / len_
    print("#{} {:.0f}".format(i, result))