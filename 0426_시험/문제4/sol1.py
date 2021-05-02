def solution(n, k) :
    if n== k :
        print(*nums)
    else :
        for i in range(n, k) :
            nums[n], nums[i] = nums[i], nums[n]
            solution(n+1, k)
            nums[n], nums[i] = nums[i], nums[n]

nums = [1,2,3]
solution(0,3)