# 동전
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input()) # 동전의 가짓 수
    lst = list(map(int, input().split())) # 만들 수 있는 동전 개수
    M = int(input()) # 목표 금액
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in lst:
        for j in range(coin,M+1): # 목표 금액 만들동안
            dp[j] = dp[j] + dp[j-coin]
            # if j<coin:
            #     dp[i][j] = dp[i-1][j]
            # else:
            #     dp[i][j] = dp[i][j-coin] + dp[i-1][j]


    # print(dp)
    print(dp[M])
