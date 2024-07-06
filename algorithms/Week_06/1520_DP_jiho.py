# 내리막길 => dfs 시간초과 나옴, dp로 풀어야되는데 정말 어렵다 이해가 될랑말랑함
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(ci, cj):
    if dp[ci][cj] == -1: # 아직 계산이 안됐다면
        # 네방향 (더 높은 곳으로부터 낮은 곳 방문 시 경로 수 누적
        dp[ci][cj] = 0 # 계산되기 위해 바꿔주기
        for dr in range(4):
            pi, pj = ci + dx[dr], cj + dy[dr] # 이전 좌표가 현재 좌표보다 클때
            if 0 <= pi < M and 0 <= pj < N and arr[pi][pj] > arr[ci][cj]:
                dp[ci][cj] += dfs(pi, pj)
    return dp[ci][cj]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*(N) for _ in range(M)]
dp[0][0] = 1
print(dfs(M-1, N-1))