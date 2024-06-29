# 바이러스 level2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def cal(K, P, N):
    MOD = 1000000007
    result = K
    # print(result)
    for i in range(1,N+1):
        # print(result)
        result = (result*P)%MOD
    return result


K, P, N = map(int, input().split())
result = cal(K,P,N)
print(result)
# print((K*P**N)%1000000007)
# ans = K*P**N
# if ans < 1000000007: print(ans)
# else: print(ans%1000000007)