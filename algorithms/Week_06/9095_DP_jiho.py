# 1,2,3 더하기 -> 진짜 점화식...
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input()) # 정수 n
    dp = [0]*(n+1)
    for k in range(1, n+1):
        if k==1:
            dp[k] = 1
        elif k==2:
            dp[k] = 2
        elif k==3:
            dp[k] = 4
        else:
            dp[k] = dp[k-3] + dp[k-2] + dp[k-1]
        # print(dp)
    print(dp[n])


