# 수퍼바이러스
import sys
import heapq
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def cal(K, P, N):
    MOD = 1000000007
    p_10 = pow(P,10,MOD)
    result = K
    # print(result)
    # for i in range(1,N+1):
    # print(result)
    result = (result*pow(p_10, N,MOD))%MOD
    return result



# 0.1초당 P배 증가 10*p
K,P,N = map(int, input().split())
result = cal(K, P, N)
print(result)