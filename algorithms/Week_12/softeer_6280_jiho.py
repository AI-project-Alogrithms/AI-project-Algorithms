# 지도 자동 구축
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [0]*16
dp[0] = 2
for i in range(1,16):
    dp[i] = (dp[i-1]-1) + dp[i-1]
# print(dp)
print(dp[N]**2)