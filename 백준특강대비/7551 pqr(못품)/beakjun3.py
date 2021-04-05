import math


# p * q를 넣었을 때 필요한 arr[r]을 구하는 메서드
def getVal(i, j):
    val = K // math.gcd(K, arr[i])
    val = val // math.gcd(val, arr[j])
    return val


def pqr(N, arr):
    # key : 필요한 arr[r]
    # val : 개수
    pq_dic = {}
    pq_dic[getVal(0, 1)] = 1

    count = 0
    for r in range(2, N):
        for pq in pq_dic:
            # arr[r]이 pd의 배수여야 한다. 최대 공약수가 pq, 즉 pd를 포함하는 수여야 한다
            if pq == math.gcd(pq, arr[r]):
                count += pq_dic[pq]
        # r을 q로 하고 i가 p라 생각. 새로운 2개 조합을 넣어주는 것
        # 있으면 개수 + 1, 없으면 새로 1
        for i in range(0, r):
            if getVal(r, i) not in pq_dic:
                pq_dic[getVal(r, i)] = 1
            else:
                pq_dic[getVal(r, i)] += 1
    return count


N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(pqr(N, arr))
