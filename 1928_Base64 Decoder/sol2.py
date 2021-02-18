import sys
sys.stdin = open("input.txt")

T = int(input())

# encoding할 때 사용하는 표
encoding_table = []
for i in range(ord('A'), ord('Z')+1):
    encoding_table.append(chr(i))
for i in range(ord('a'), ord('z')+1):
    encoding_table.append(chr(i))
for i in range(10):
    encoding_table.append(str(i))
encoding_table.append('+')
encoding_table.append('/')

for tc in range(1, T+1):
    # 인코딩 된 문자열
    encoding_string = list(input())
    # 표를 보고 문자로 인코딩 하기 전의 값이 들어갈 리스트
    before_encoding = []
    for i in range(len(encoding_string)):
        for j in range(len(encoding_table)):
            # encdoing된 문자열의 값이 표의 숫자 값으로
            if encoding_string[i] == encoding_table[j]:
                before_encoding.append(j)

    # before_encoding의 값을 binary로 바꾸기
    bin_encoding = ''
    # 마지막 숫자인 63을 2진수로 변환하면 111111.
    # 6개를 기준으로 그보다 작은 숫자는 앞을 0으로 채운다.
    for i in before_encoding:
        bin_encoding += (6-len(bin(i)[2:])) * '0' + str(bin(i)[2:])

    # 1비트는 8byte기 때문에?
    result = ''
    for i in range(len(bin_encoding)//8):
        result += chr(int(bin_encoding[:8], 2))
        bin_encoding = bin_encoding[8:]

    print("#{} {}".format(tc, result))
