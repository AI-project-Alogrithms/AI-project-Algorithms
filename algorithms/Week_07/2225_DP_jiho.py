# 합문해
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution():
    for i in range(1,k):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # for i in dp:
        # print(i)
    print(dp[-1][-1]%1000000000) # 나누기 안해서 틀림.. 점화식은 맞았다.ㅎ

n, k = map(int, input().split())
dp = [[1]*(n+1)] + [[1] + [0] * n for _ in range(k-1)]
# dp = [[1] * (n + 1) for _ in range(k)]
# for i in dp:
#     print(i)
solution()