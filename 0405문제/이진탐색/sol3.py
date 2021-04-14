
def inorder(node):
    global cnt
    if node > 0:
        inorder(node_input[node][0])
        node_input[node][3] = cnt
        cnt += 1
        inorder(node_input[node][1])

for tc in range(1, T+1):
    N = int(input()) # 1~N까지 이진탐색 트리에 저장
    node_input = [[0, 0, x//2, 0] for x in range(N+1)] # 왼쪽 자식, 오른쪽 자식, 부모, 값
    for i in range(1, N+1):
        if 2*i < N+1:
            node_input[i][0] = 2*i
        if 2*i+1 < N+1:
            node_input[i][1] = 2*i+1

    cnt = 1
    inorder(1)
    # print(node_input)

    print("#{} {} {}".format(tc, node_input[1][3], node_input[N//2][3]))