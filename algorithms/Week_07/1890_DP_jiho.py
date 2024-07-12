# 점프
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution():
    for i in range(n):
        for j in range(n):
            if dp[i][j] > 0 and arr[i][j] !=0: # 해당 값이 존재하고(jump위치 도달), 목표지점이 아니면
                jump = arr[i][j]
                # 오른쪽으로 점프
                if j+jump < n: # 범위내
                    dp[i][j+jump] += dp[i][j]
                # 아래로 점프
                if i+jump < n:
                    dp[i+jump][j] += dp[i][j]
    print(dp[-1][-1])

n=int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp[0][0] = 1
solution()
# for i in dp:
#     print(i)
