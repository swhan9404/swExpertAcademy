import sys
sys.stdin = open("input.txt")

from collections import deque

T = 10

# qeueue 이용 = 183 ms 실행시간
for tc in range(1, T+1):
    nothing = input()
    inp_arr = list(map(int, input().split()))

    queue = deque(inp_arr)
    i =0
    while True :
        front = queue.popleft() # 맨 앞 값 뺴오기
        front -= (i%5)+1 # 순서만큼 빼주기
        if front <= 0 :
            front = 0
            queue.append(front)
            break
        queue.append(front) # 다시 넣기
        i+=1 # 순서 증가

    result = " ".join(map(str, queue))
    
    print("#{} {}".format(tc, result))

