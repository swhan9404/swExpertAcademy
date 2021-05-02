T = int(input())

def binary_search(start, end, find, cnt) : # 이진 탐색
    global min_cnt
    global min_result

    cnt+=1 # 몇번 했는지 카운팅
    mid = (start+end)//2 # 가운데 위치
    if inp_arr[mid] == find : # 가운데 위치의 것이 찾는 것일 때 끝냄
        if min_cnt > cnt :
            min_cnt = cnt
            min_result = inp_arr[mid]
        return
    elif mid == start : # 가운데 인덱스가 시작 인덱스랑 같을 때 끝냄(무한루프방지)
        return

    binary_search(start, mid-1, find, cnt)
    binary_search(mid, end, find, cnt)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 숫자 갯수
    # M : 탐색할 숫자 갯수
    search_arr = list(map(int, input().split()))
    inp_arr = list(map(int, input().split()))

    min_cnt = 987654321 # 최대 탐색횟수
    min_result = 0

    for i in range(len(search_arr)) :
        tmp_cnt = binary_search(0, len(inp_arr)-1, search_arr[i], 0)


    print("#{} {} {}".format(tc, min_result, min_cnt))

