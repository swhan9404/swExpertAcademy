import sys
# stdin = standard input 표준입력
sys.stdin = open('input.txt') # input 파일 불러옴

N = int(input())

result = 1 if N%2 else 0
print(result)

inp_arr = list(map(int, input().split()))
print(sum(inp_arr))

N = int(input())
result = list()
for _ in range(N) :
    result.append(list(map(int, input().split())))
print(result[1][1])