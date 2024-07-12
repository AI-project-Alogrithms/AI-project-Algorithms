# 파도반 수열
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution(dp):
    dp[0], dp[1], dp[2] = 1, 1, 1
    if n==1 or n==2 or n==3:
        return dp[n-1]
    for i in range(3,n):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[n-1]

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0]*(n+3) # n=1,2,3 일때도 만들어지긴 하도록 3개 dp 더 만들기

    print(solution(dp))