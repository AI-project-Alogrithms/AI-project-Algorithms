# 동전 1 -> 어렵다
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
dp = [0]*(k+1) # 최대 가치 만큼
dp[0] = 1 # 동전 한개만 사용했을 때 경우의 수

for i in lst:
    for j in range(i,k+1):
        # print(dp)
        dp[j] = dp[j] + dp[j-i]
print(dp[k])
