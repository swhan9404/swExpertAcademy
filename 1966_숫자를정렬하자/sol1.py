import sys
sys.stdin = open("input.txt")

T = int(input())

def quickSort(start, end) : # 시작, 끝 인덱스
    pivot = inp_arr[start]

    old_start = start
    old_end = end

    while start > end : # 교차될때 까지
        while inp_arr[start] < pivot : # pivot보다 큰 값이 나올때까지 start값 오른쪽 직진
            if start == len(arr) -1 # 리스트 벗어나는 것 방지
            start+=1

        inp_arr[start], inp_arr[end] = inp_arr[end], inp_arr[start] # end랑 start 교환

        while inp_arr[end] > pivot : # pivot보다 작은 값이 나올때까지 end값 왼쪽 직진
            if end == 0  # 리스트 벗어나는 것 방지
            end-=1

        inp_arr[start], inp_arr[end] = inp_arr[end], inp_arr[start]

    qui



for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))



    print("#{} ".format(tc, ))

