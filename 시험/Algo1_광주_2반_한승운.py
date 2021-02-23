T = int(input())

for tc in range(1, T+1) :
    # N : 행크기
    # M : 열크기
    N, M = map(int,input().split())

    inp_arr = [list(map(int, input().split())) for _ in range(N)]

    # 심는 총 비용
    total_cost = 0

    # 심은 나무 수
    tree_cnt = ((M + 1) // 2) * N

    # 가장 비싼 나무 가격
    high_tree_cost = 0

    # 가장 비싼 나무 심어진 열 번호( 문제는 1로 시작하지만, 코드 내에서는 0 부터 시작하니 마지막에 1 더해주기)
    high_tree_idx = 0

    for y in range(N) : # inp_arr 전체를 돌면서
        for x in range(0, M, 2) : # 0~M 을 간격 2로
            tmp_cost = inp_arr[y][x] # 여러번 써야 하기 때문에 배열 접근 최소화를 위해 변수에 담기
            total_cost += tmp_cost
            if high_tree_cost < tmp_cost :
                high_tree_cost = tmp_cost
                high_tree_idx = x
            elif high_tree_cost == tmp_cost and high_tree_idx < x: # 같은 숫자일시 열번호 더 큰것 우선
                high_tree_idx = x

    # 결과 출력
    print("#{} {} {} {} {}".format(tc, total_cost, tree_cnt, high_tree_cost, high_tree_idx+1))