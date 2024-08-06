# 단기간 성장: 평범한 배낭
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
lst = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x:x[0])
# print(lst)
dp = [[0] * (K+1) for _ in range(N+1)]
# print(dp)
for i in range(1,N+1):
    for j in range(1,K+1):
        if lst[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][0]]+lst[i][1])
print(dp[-1][-1])
