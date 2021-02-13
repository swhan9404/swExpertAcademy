import sys
sys.stdin = open("input.txt")

T = int(input())

def quickSort(start, end) : # 시작, 끝 인덱스

    # 첫 시작점, 끝점 기억
    old_start = start
    old_end = end

    # 함수의 종료부분 : 길이차이가 1 이하일때
    if end - start <= 1 :
        if inp_arr[start] > inp_arr[end] :
            inp_arr[start], inp_arr[end] = inp_arr[end], inp_arr[start]
        return

    # pivot 잡기
    pivot = inp_arr[start]
    start +=1 # pivot 다음 점부터 시작

    while start <= end : # start와 end가 교차되면 끝냄
        while inp_arr[start] < pivot and start < end : # old_start 에서 오른쪽으로가면서 pivot보다 큰값 찾기
            start+=1
        while inp_arr[end] >= pivot and end > start : # old_end에서 왼쪽으로 가면서 pivot보다 작은값 찾기 (= 빠지면 같은값 3개가 존재할 경우 무한 루프 도니 주의)
            end-=1

        if start >= end :
            break

        # 찾은 값들 자리 서로 교환하기
        inp_arr[start], inp_arr[end] = inp_arr[end], inp_arr[start]

    # 피벗과 가장 작은 부분 마지막과 교환
    small_last = 0


    if inp_arr[start] >=pivot :
        small_last = start - 1
    else :
        small_last = start

    inp_arr[old_start], inp_arr[small_last] = inp_arr[small_last], inp_arr[old_start]

    # 작은 부분과 큰 부분 따로 sort 다시 돌려주기
    # if 빠지면 가끔 3개로 이뤄진 부분에서 인덱스 밖으로 튕겨져 나가는 에러가 나올 수 있어서 막아줌
    if old_start < small_last :
        quickSort(old_start, small_last-1)
    if old_end > small_last :
        quickSort(small_last+1, old_end)
    return



for tc in range(1, T+1):
    N = int(input())
    inp_arr = list(map(int, input().split()))
    quickSort(0, len(inp_arr)-1)

    result = map(str, inp_arr)
    result = " ".join(result)
    print("#{} {}".format(tc, result))

