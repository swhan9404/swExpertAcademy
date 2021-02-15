import sys
sys.stdin = open("input.txt")

# 8bit = 1 byte
# 영.특문 글자당 = 1byte

def decode(x) : # 글씨 받아서 코드값 반환
    if ord("A") <= ord(x) <= ord("Z") :
        return ord(x)-ord("A")
    elif ord("a") <= ord(x) <= ord("z") :
        return ord(x)-ord("a")+26
    elif ord("0") <= ord(x) <= ord("9") :
        return ord(x)-ord("0")+52
    elif ord("+") == ord(x) :
        return 62
    elif ord("/") == ord(x) :
        return 63

T = int(input())

for tc in range(1, T+1):
    inp = input()
    print("#{} ".format(tc), end="")

    n = 0
    while n < len(inp) :
        binary_code = ""

        # 디코딩해서 4글자의 코드값 가져오기
        while n < len(inp) :
            code = '{:06b}'.format(decode(inp[n]))
            binary_code += code
            n+=1
            if n%4 == 0 :
                break

        # 코드값 글씨 만들기
        k=0
        while k < len(binary_code):
            code =binary_code[k:k+8]
            text = chr(int('0b'+code, 2))
            print(text, end="")
            k+=8

    print()
