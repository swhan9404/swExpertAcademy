import sys
sys.stdin = open("input.txt")

T = int(input())
def KMP(word, pattern):

    W = len(word)
    P = len(pattern)

    def pi(end):  # pattern 위치별 pi 판단 끝 인덱스
        max_pi = 0

        for i in range((end+1)//2):
            if pattern[:i+1] == pattern[end-i:end+1]:
                max_pi = i+1
        return max_pi

    word_idx = 0
    pattern_idx = 0
    pattern_pi_list = [pi(i) for i in range(P)] # pattern 위치별 pi 리스트 작성

    while word_idx < W and pattern_idx < P:
        # 밑에 주석 위치
        if word[word_idx] != pattern[pattern_idx]:
            word_idx -= 1 if pattern_idx!=0 else 0 # word_idx는 그대로
            pattern_idx = pattern_pi_list[pattern_idx-1] -1 # pattern_idx만 pi만큼 뒤로 보내줌

        word_idx += 1
        pattern_idx += 1
    """실제동작
    print(word_idx, word[word_idx], pattern[pattern_idx], pattern_idx)
    0 A A 0
    1 B B 1
    2 C C 2
    3 D D 3
    4 A A 4
    5 B B 5
    6 C E 6
    6 C C 2
    7 D D 3
    8 A A 4
    9 B B 5
    10 E E 6
    """

    if pattern_idx == P:
        return 1  # 검색성공
    else:
        return 0  # 검색실패

for tc in range(1, T+1):
    pattern = input()
    word = input()
    result = KMP(word, pattern)

    print("#{} {}".format(tc, result))

