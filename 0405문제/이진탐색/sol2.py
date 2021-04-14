import sys
sys.stdin = open("input.txt")

T = int(input())

def make_tree(n) :
    global cnt
    left_child = n*2
    right_child = n*2 +1

    if left_child <= N :
        make_tree(left_child) # 왼쪽 자식노드

    tree[n] = cnt
    cnt+=1

    if right_child <= N:
        make_tree(right_child) # 오른쪽 자식노드

for tc in range(1, T+1):

    N = int(input())
    tree = [0] *(N+1)
    cnt = 1
    make_tree(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))

