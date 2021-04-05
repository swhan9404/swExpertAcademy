# 거꾸로 접근해서 풀기
S = input()
T = input()

while len(S) < len(T) :
    if T[-1]  == 'A' :
        T = T[:-1]
    elif T[-1] == 'B' :
        T = T[-2::-1]

if S == T :
    print(1)
else :
    print(0)
