# 벼락치기: 0-1 배낭문제
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, T = map(int, input().split())
lst = [[0]]+ [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1, N+1):
    time, s = lst[i][0], lst[i][1]
    # print(time, s)
    for j in range(1,T+1):
        if time > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-time]+s, dp[i-1][j])
    # print(dp)
print(dp[N][T])