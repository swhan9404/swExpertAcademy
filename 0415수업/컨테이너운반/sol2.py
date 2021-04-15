import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 컨테이너수
    # M : 트럭수
    container_arr = list(map(int, input().split()))
    truck_arr = list(map(int, input().split()))
    visited = [0] * len(container_arr)

    container_arr.sort(reverse=True)
    truck_arr.sort(reverse=True)

    result = 0
    for i in range(len(truck_arr)) :
        for j in range(len(container_arr)) :
            if truck_arr[i] >= container_arr[j] :
                tmp_container = container_arr.pop(j)
                truck_arr[i] -= tmp_container
                result+= tmp_container
                break

    print("#{} {}".format(tc, result))

