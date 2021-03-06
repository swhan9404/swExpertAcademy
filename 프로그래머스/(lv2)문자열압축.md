

# 1. 정해진 길이만큼 아니게 잘릴 경우

- x / ababcdcd / ababcdcd 

  이렇게 잘릴 게 가능할 경우

```python
def solution(s):
    
    result = len(s)
    
    for cut in range(1, len(s)//2 +1) :
        tmp_length = 0
        i = 0 # 탐색 시작 위치
        while i<len(s) : # 전체 순회하면서  
            if (i+2*cut)<=(len(s)+1) and s[i:i+cut] == s[i+cut:i+2*cut] :
                cnt = 1
                for tmp_idx in range(i+cut, len(s), cut) :
                    if tmp_idx+2*cut<=len(s) and s[tmp_idx:tmp_idx+cut] == s[tmp_idx+cut:tmp_idx+2*cut] :
                        cnt +=1
                    else :
                        break
                i+= cut*(cnt+1) # 시작 인덱스 옮기기
                tmp_length += cut+1 # 길이 늘려주기
            else : 
                i+=1
                tmp_length +=1
        else :
            if tmp_length < result :
                result = tmp_length

    return result
```



# 2. 풀이

```python
def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s) // 2 + 1): 
        count = 1
        tempStr = s[:cut] 
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
    
    return min(length)
```

