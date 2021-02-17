import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    ttc, N = input().split()
    N = int(N)

    word_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    def decode(x) :
        for idx in range(len(word_list)) :
            if word_list[idx] == x :
                return idx
    def encode(x) :
        return word_list[x]

    def mergeSort(arr) :
        if len(arr) <= 1 :
            return arr
        mid = len(arr) //2
        leftList = arr[:mid]
        rightList = arr[mid:]

        leftList = mergeSort(leftList)
        rightList= mergeSort(rightList)
        return merge(leftList, rightList)

    def merge(left, right):
        result = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
            elif len(left) > 0:
                result.append(left[0])
                left = left[1:]
            elif len(right) > 0:
                result.append(right[0])
                right = right[1:]
        return result

    inp_arr = list(map(decode, input().split()))
    inp_arr = mergeSort(inp_arr)
    inp_arr = map(encode, inp_arr)
    result = " ".join(inp_arr)

    print("#{} {}".format(tc, result))

