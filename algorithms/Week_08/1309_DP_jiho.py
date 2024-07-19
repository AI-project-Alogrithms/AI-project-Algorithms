# 동물원
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())

if n==1:
    print(3)
else:
    dp = [1] * (n + 1)
    dp[1], dp[2] = 3, 7
    for i in range(3,n+1):
        dp[i] = (2*dp[i-1] + dp[i-2])%9901# ((dp[i-1]-dp[i-2])*2+(2*(i-2)) + dp[i-1])%9901
    print(dp[n])