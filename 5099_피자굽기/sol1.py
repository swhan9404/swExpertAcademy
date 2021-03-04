import sys
sys.stdin = open("input.txt")

from collections import deque
T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    inp_arr = list(map(int, input().split())) # 피자마다의 치즈

    queue = deque(range(N))
    i = N # 몇번째 피자까지 넣었는지

    while len(queue)>1 : # 큐가 하나 남을때까지
        idx = queue.popleft()
        inp_arr[idx] //=2 # 치즈 녹이기
        if inp_arr[idx] == 0 : # 다 구워지면 빼고
            if i <M :
                queue.append(i) # 다음피자 넣고
                i+=1
            continue
        queue.append(idx) # 아니면 다시 넣고

    result = queue.popleft()
    result +=1 # 인덱스 맞춰주기
    print("#{} {}".format(tc, result))

