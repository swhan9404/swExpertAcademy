# input
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 1->2, 1->3 이라는 의미임
input1 = "13"
input2 = "1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13"

V =int(input1) # int(input())
E = V-1

temp = list(map(int, input2.split()))
tree = [ [0,0,0] for _ in range(V+1) ]

def preorder_traverse(node) :
    if node != 0 :
        print('{}'.format(node), end=' ')
        print('{}'.format(tree[node][0]))
        print('{}'.format(tree[node][1]))

for i in range(E) :
    # [0, 0, 0] => [왼쪽자식, 오른쪽자식, 부모노드]
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0] : #왼쪽 자식의 자리가 비어있다면
        tree[parent][0] = child
    else :
        tree[parent][1] = child
    tree[child][2] = parent
    print(preorder_traverse(1))

