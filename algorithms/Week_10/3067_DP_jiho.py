# Coins: 배낭문제
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def program_count(lst, dp):
    for i in range(1,N+1):
        for j in range(1,M+1):
            if lst[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-lst[i]] + dp[i-1][j]
    return dp[-1][-1]

T = int(input())
for _ in range(T):
    N = int(input()) # 동전의 가지 수
    lst = list(map(int, input().split()))
    lst = [0] + lst
    M = int(input())
    dp = [[1] + [0]*(M) for _ in range(N+1)]
    print(program_count(lst, dp))
