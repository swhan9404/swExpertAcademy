# https://www.acmicpc.net/problem/12871
inp1 = input()
inp2 = input()

if len(inp1) > len(inp2) : # inp2 길이가 항상 길게
    inp1, inp2 = inp2, inp1

inp2 = inp2 * 2
"""
ab
ababa
걸러내기 위함
"""

inp1_idx = inp2_idx = 0
while inp2_idx <len(inp2) :
    if inp1[inp1_idx] == inp2[inp2_idx] :
        inp1_idx = (inp1_idx+1) % len(inp1)
        inp2_idx+=1
    else :
        print(0)
        break
else :
    print(1)