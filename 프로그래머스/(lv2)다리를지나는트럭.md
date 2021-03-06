```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length) 
    
    time = 0
    queue_sum = 0 # sum 을 계속 쓰면 시간초과발생
    while truck_weights :
        queue_sum -= queue.popleft() # 일단 빼기

        if queue_sum+truck_weights[0] <= weight : 
            tmp_value = truck_weights.pop(0)
            queue_sum += tmp_value
            queue.append(tmp_value)
        else :
            queue.append(0)
        time+=1
    
    time+=bridge_length
    return time
```

