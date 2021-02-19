import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    inp = input()

    group = ["S","D","H","C"]
    dic = {
        x : set() for x in group
    }

    for i in range(0, len(inp), 3) :
        pick_group = dic[inp[i]]
        before= len(pick_group)
        pick_group.add(inp[i+1:i+3])
        after = len(pick_group)
        if before == after :
            result = "ERROR"
            break
    else :
        result = ""
        for key in group :
            result+= str(13-len(dic[key])) + " "
        result.rstrip()
    print("#{} {}".format(tc, result))


