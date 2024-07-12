# 스티커
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution(dp):
    # 스티커가 1개라면
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n==1:
        return max(dp[0][n-1], dp[1][n-1])
    # 스티커가 2개라면
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n==2:
        return max(dp[0][n-1], dp[1][n-1])
    # 스티커가 3개 이상이라면
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
    # print(dp)
    return max(dp[0][n-1], dp[1][n-1])

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)] # 누적할 dp 만들기
    print(solution(dp))