```Python
def pri_max(priorities, arr_idx) :
    M = 0
    for idx in arr_idx :
        if priorities[idx] > M :
            M = priorities[idx]
    return M

def solution(priorities, location):
    N = len(priorities) # 길이
    idx_arr = list(range(N))
    count =0
    
    while idx_arr :
        now_idx = idx_arr.pop(0)
        M = pri_max(priorities, idx_arr) # 최고 중요도
        if M>priorities[now_idx] : # 다시 집어넣기
            idx_arr.append(now_idx)
        else : #다시 안집어넣었을 경우
            count+=1
            if now_idx == location :
                return count
```

