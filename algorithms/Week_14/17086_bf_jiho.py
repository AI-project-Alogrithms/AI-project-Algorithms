# 아기상어
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
# 그 칸과 가장 거리가 가까운 아기 상어와의 거리
def bfs(i,j):
    q = deque()
    q.append((i,j))
    dp = [[-1]*m for _ in range(n)]
    dp[i][j] = 0
    while q:
        ci, cj = q.popleft()
        for i in range(8):
            ni, nj = ci+dx[i], cj+dy[i]
            if 0<=ni<n and 0<=nj<m and dp[ni][nj]==-1:
                dp[ni][nj] = dp[ci][cj]+1
                q.append((ni,nj))
    # for i in dp:
    #     print(i)
    value = 1000
    for i,j in shark:
        # print(dp[i][j])
        value = min(value, dp[i][j])
    return value


dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

shark = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            shark.append((i,j))
# print(shark)
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1: continue # 아기상어라면 패스
        # print("i,j", i,j)
        ans = max(ans, bfs(i,j))
print(ans)