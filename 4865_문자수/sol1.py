import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    str1 = input()
    str2 = input() # 더 긴거

    word_dic = {
        tmp: 0 for tmp in str1
    }

    result = 0 # max_cnt
    for tmp in str2 :
        cnt = word_dic.get(tmp, -1)+1
        if cnt : # str1 에 없었던 것은 dic에 추가 안되기 위함
            word_dic[tmp] = cnt
        if result < cnt :
            result = cnt

    print("#{} {}".format(tc, result))

