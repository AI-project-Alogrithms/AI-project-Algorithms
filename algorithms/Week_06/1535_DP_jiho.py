# 안녕
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0]*100 for _ in range(N+1)]

for i in range(1,N+1): # 사람 돌동안
    for j in range(100):
        if L[i] > j: # 해당 체력 미만이라면
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-L[i]]+J[i], dp[i-1][j])
    # print(dp)
print(dp[N][99])