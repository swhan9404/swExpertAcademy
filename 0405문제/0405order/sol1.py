N = int(input())

def tree_num(N) :
    """
    [
        0 [0,0,0], // 왼쪽, 오른쪽, 부모
        1 [2,3,0],
    ]
    """
    tree_arr = [0] * (N+1)

    for i in range(1, N+1) :
        next_left = 2*i if 2*i <= N else 0
        next_right = 2*i+1 if 2*i+1 <= N else 0
        parent = i//2 if i//2 >0 else 0

        tree_arr[i] = [next_left, next_right, parent]

    return tree_arr

print(tree_num(N))