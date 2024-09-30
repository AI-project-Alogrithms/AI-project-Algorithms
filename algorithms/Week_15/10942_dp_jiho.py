# 팰린드룸
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)] # 미리 저장

# i==j==1
for i in range(n):
    dp[i][i] = 1

# 두번째자리까지의 비교
for i in range(n-1):
    if lst[i]==lst[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0
# 나머지 비교
for row in range(n-2): # 채워지지 않은 나머지 행 돌동안
    for i in range(n-2-row): # 채워지지 않은 나머지 열 돌기
        j = i+2+row # 그때의 열 번호
        if lst[i]==lst[j] and dp[i+1][j-1]==1:
            dp[i][j] = 1

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
