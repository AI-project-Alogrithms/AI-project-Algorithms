# 파이프 옮기기1 -> dp임, 그래프 탐색으로 하면 시간초과 남
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
# # Check if the file can be opened
# try:
#     sys.stdin = open(r"C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
# except FileNotFoundError:
#     print("Error: File not found. Please check the file path.")
#     sys.exit(1)
input = sys.stdin.readline
from collections import deque


def dfs():
    # 1 행 미리 처리하기
    dp[0][0][1] = 1 # 처음 들어가는 곳
    for i in range(2, N): # 가로로 가는 경우는 한가지 밖에 없음
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    # 1열로 가는 경우는 없으니 제외하고 돌기 (1행은 위에서 미리 처리함)
    for r in range(1,N):
        for c in range(1,N):
            # 대각선에 파이프 추가
            if board[r][c] == 0 and board[r][c-1] == 0 and board[r-1][c] == 0:
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            # 가로, 세로 파이프 추가
            if board[r][c] ==0:
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1] # 가로 파이프 추가
                dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c] # 세로 파이프 추가
        # print(dp)
    print(sum(dp[i][N-1][N-1] for i in range(3)))




N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 가로, 대각선, 세로 DP
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# print(dp)
dfs()