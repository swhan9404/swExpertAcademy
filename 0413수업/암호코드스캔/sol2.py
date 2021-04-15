import sys
sys.stdin = open("input.txt")

T = int(input())

# 코드 확인
def code_check(encode_data_join) :
    global result
    bin_to_num = []
    f, s, t = 0, 0, 0

    for i in range(len(encode_data_join)-1, -1, -1) :
        if s == 0 and t == 0 and encode_data_join[i] == '1':
            f += 1
        elif f != 0 and t == 0 and encode_data_join[i] == '0':
            s += 1
        elif f != 0 and s != 0 and encode_data_join[i] == '1':
            t += 1
        elif t != 0 and encode_data_join[i] == '0':
            minn = min(f, s, t)
            res_fst = str(f // minn) + str(s // minn) + str(t // minn)
            bin_to_num.append(code[res_fst]) # 없는 코드가 들어올경우

            f, s, t = 0, 0, 0  # 초기화

        if len(bin_to_num) == 8:
            tmp_num = ''.join(map(str,bin_to_num))
            if visited.get(tmp_num, 1) :
                visited[tmp_num]=0  # 방문체크
                if ((bin_to_num[1] + bin_to_num[3] + bin_to_num[5] + bin_to_num[7]) * 3 + bin_to_num[0] + bin_to_num[2] + bin_to_num[4] + bin_to_num[6]) % 10 == 0:
                    result += sum(bin_to_num)
                    bin_to_num.clear()

def find_endcoding(line) :
    if visited2.get(line, 1):
        visited2[line] = 0
        encode_data = [hex[x] for x in line]
        encode_data_join = ''.join(encode_data) # 여기까지가 코드 인코딩

        code_check(encode_data_join.rstrip('0'))


for tc in range(1, T+1):
    N, M = map(int, input().split())
    inp_arr = [input()[:M] for _ in range(N)]
    code = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
    hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    visited2 = {} # 같은 입력코드
    visited= {} # 변환된 코드
    result = 0

    for line in inp_arr :
        find_endcoding(line)


    print("#{} {}".format(tc, result))

