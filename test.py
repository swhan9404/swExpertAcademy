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
    pattern_list = set(pattern) # 보이어 무어 적용 용도

    while word_idx < W and pattern_idx < P:
        word_idx += P-1
        pattern_idx = P-1

        for i in range(P) :
            if word[word_idx-i] not in pattern_list :
                break
            if word[word_idx-i] != pattern[pattern_idx-i] :
                word_idx -= pattern_pi_list[pattern_idx-i]
                pattern_idx = - pattern_pi_list[pattern_idx-i]
        else :
            pattern_idx = P

    """실제동작
    print(word_idx, word[word_idx], pattern[pattern_idx], pattern_idx)
    0 A A 0
    1 B B 1
    2 C C 2
    3 D D 3
    4 A A 4
    5 B B 5
    6 C E 6  - 달라짐
    6 C C 2  - pattern idx만 맞춰줌
    7 D D 3
    8 A A 4
    9 B B 5
    10 E E 6
    """

    if pattern_idx == P:
        return word_idx - P  # 검색성공
    else:
        return -1

print(KMP("ABCDABCDABEE", "ABCDABE"))