# 앱: 0-1 배낭문제
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
byte_lst = [0] + list(map(int, input().split()))
cost_lst = [0] + list(map(int, input().split()))
length = sum(cost_lst)+1
dp = [[0]*length for _ in range(N+1)]
ans = length+1
for i in range(1,N+1):
    byte, cost = byte_lst[i], cost_lst[i]
    # print(byte, cost)
    for j in range(length):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else: # j가 cost보다 크거나 같다면
            dp[i][j] = max(dp[i-1][j-cost]+byte, dp[i-1][j]) # 해당 앱을 종료 시켰을 경우와 종료 시키지 않았을 경우 중에 비교
        if dp[i][j] >= M:
            ans = min(ans, j)
print(ans)

