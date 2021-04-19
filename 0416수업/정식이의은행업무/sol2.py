import sys
sys.stdin = open("input.txt")

T = int(input())

def to_int(code,n) :
    result = 0
    for i in range(len(code)) :
        result+= code[i] * n ** (len(code) -1 -i)
    return result

def binary(bin) :
    bin_list = []
    for i in range(len(bin)) :
        bin[i] = 0 if bin[i] else 1
        bin_list.append(to_int(bin, 2))
        bin[i] = 0 if bin[i] else 1
    return bin_list

def triple(tri) :
    tri_list = []
    for i in range(len(tri)) :
        origin = tri[i]
        for j in range(3) :
            if tri[i] != j :
                tri[i] = j
                tri_list.append(to_int(tri, 3))
                tri[i] = origin
    return tri_list


for tc in range(1, T+1):
    bin = list(map(int,list(input())))
    tri = list(map(int,list(input())))

    bin_list = binary(bin)
    tri_list = triple(tri)

    result = 0
    for tmp in bin_list :
        if tmp in tri_list :
            result = tmp
            break

    print("#{} {}".format(tc, result))

