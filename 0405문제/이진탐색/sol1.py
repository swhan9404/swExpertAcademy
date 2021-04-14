import sys
sys.stdin = open("input.txt")

T = int(input())

class Node :
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinartSearchTree :
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._inset_value(self.root, data)
        return self.root is not None

    def _inset_value(self, node, data):
        if node is None :
            node = Node(data)
        else :
            if data <= node.data :
                node.left = self._inset_value(node.left, data)
            else :
                node.right = self._inset_value(node.right, data)
        return node


for tc in range(1, T+1):
    N = int(input())

    # result1 = 2 ** int(N ** (1/2))
    # result2 =
    binary_tree= BinartSearchTree()
    for i in range(1, N+1) :
        binary_tree.insert(i)

    print("#{} {}".format(tc, binary_tree.root.data))

