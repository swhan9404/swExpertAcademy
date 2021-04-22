import sys
sys.stdin = open("input.txt")

T = int(input())

# 리스트 다 만들어서 할 시에 메모리 초과
def merge_sort(arr) :
    if len(arr) == 1 :
        return arr
    left = arr[:len(arr)]
    right = arr[len(arr):]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right) :
    global cnt
    if left[-1] > right[-1] :
        cnt+=1
    result =[]
    while len(left) >0 or len(right) >0 :
        if len(left) >0 and len(right) >0 :
            if left[0] <= right[0] :
                result.append(left.pop(0))
            else :
                result.append(right.pop(0))
        elif len(left) > 0 :
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))
    return result

for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))
    cnt = 0

    sorted_arr = merge_sort(inp_arr)
    result1 = sorted_arr[N//2]
    print("#{} {} {}".format(tc, result1, cnt))

