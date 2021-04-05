import sys
sys.stdin = open("input.txt")

T = 10

def inorder_traverse(x ,inp_arr) :
    tmp = inp_arr[x]

    try :
        inorder_traverse(int(tmp[2]), inp_arr)
    except :
        pass

    print("{}".format(tmp[1]), end="")

    try:
        inorder_traverse(int(tmp[3]), inp_arr)
    except:
        pass


for tc in range(1, T+1):
    N = int(input())
    inp_arr =[0]* (N+1)
    for _ in range(N) :
        tmp_arr = input().split()
        inp_arr[int(tmp_arr[0])] = tmp_arr



    print("#{} ".format(tc, ))
    inorder_traverse(1, inp_arr)
    print()
