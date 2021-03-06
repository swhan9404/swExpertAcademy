```python
def solution(new_id):
    stage1 = new_id.lower()
    stage2 = [x for x in stage1 if x.isalpha() or x.isdigit() or (x in ["-", "_", "."])] 
    stage3 = [stage2[0]]+[stage2[x] for x in range(1,len(stage2)) if not (stage2[x-1]=="." and stage2[x]==".")]

    stage4 = stage3
    if stage4 and stage4[0] == "." :
        stage4.pop(0)
    if stage4 and stage4[-1] == "." :
        stage4.pop(-1)
    
    stage5 = "a" if len(stage4)==0 else "".join(stage4)
    stage6 = stage5[:15]
    stage6 = stage6.strip(".")
        
    stage7 = stage6
    while len(stage7) <=2 :
        stage7 += stage7[-1]

    return stage7
```

