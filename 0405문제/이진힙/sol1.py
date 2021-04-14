import sys
sys.stdin = open("input.txt")

T = int(input())

class Node :
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

class Tree :
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_val(self.root, data)
        return self.root

    def _insert_val(self, root, data):
        if root is None :
            root = Node(data)
        else :
            if data < root.data :
                root.left = self._insert_val(root.left, data)
            else :
                root.right = self._insert_val(root.right, data)
        return root

    def leaf_sum(self):






for tc in range(1, T+1):
    N = int(input())

    inp_arr = list(map(int, input().split()))

    print("#{} ".format(tc, ))

