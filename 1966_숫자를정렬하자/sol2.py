import sys
sys.stdin = open("input.txt")

T = int(input())

# 본래 의미의 quickSort
def quickSort(arr) :
    if len(arr) <= 1 :
        return arr

    pivot = arr[len(arr) // 2] # 중간값을 pivot

    low_arr =[]
    equal_arr =[]
    high_arr = []

    for tmp in arr :
        if tmp < pivot :
            low_arr.append(tmp)
        elif tmp == pivot :
            equal_arr.append(tmp)
        else :
            high_arr.append(tmp)

    return quickSort(low_arr) + equal_arr + quickSort(high_arr)

# list 계속 생성 안하는 버전으로
def quickSort2(arr) :
    def sort(low, high) :
        if high <= low :
            return

        mid = partition(low, high)
        sort(low, mid -1)
        sort(mid, high)

    def partition(low, high) :
        pivot = arr[(low+high) // 2]
        while low <= high :
            while arr[low] < pivot :
                low+=1
            while arr[high] > pivot :
                high -=1
            if low <= high :
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low+1, high-1
        return low
    return sort(0, len(arr) -1 )


for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))
    quickSort2(inp_arr)

    result = map(str, inp_arr)
    result = " ".join(result)
    print("#{} {}".format(tc, result))


