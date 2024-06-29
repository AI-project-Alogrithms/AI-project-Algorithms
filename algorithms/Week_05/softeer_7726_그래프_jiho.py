# 나무섭지
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

# 유령이 먼저 목적지에 도착하면 실패, 남우가 아무리 해도 도착안하면 실패
def bfs(f, i,j):
    q = deque()
    q.append((i,j))
    # gi, gj = g[0], g[1]
    # gq = deque()
    # gq.append((gi, gj))
    dp[i][j] = 1
    # gp[i][j] = 1
    while(q):
        ci, cj = q.popleft()
        if arr[ci][cj] == 'D':
            # print(dp[ci][cj])
            return dp[ci][cj]-1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and dp[ni][nj] == 0:
                if f==0 and arr[ni][nj] != '#': # 범위내, 미방문, 벽 아님, 남우이면
                    dp[ni][nj] = dp[ci][cj] + 1 # 방문 표시
                    # print(dp)
                    q.append((ni, nj))
                if f==1: # 유령이면
                    dp[ni][nj] = dp[ci][cj] + 1 # 방문 표시
                    # print(dp)
                    q.append((ni, nj))
    return 'No'

n,m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
# gp = [[0]*m for _ in range(n)]
# print(arr)
g = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D': # 출구
            fi, fj = i, j
        if arr[i][j] == 'N': # 남우가 있는 곳
            ci, cj = i, j
        if arr[i][j] == 'G': # 유령이면
            g.append((i,j))
dis = []
for i in range(len(g)):
    gi, gj  = g[i][0], g[i][1]
    g_dis = abs(fi-gi) + abs(fj-gj)
    dis.append(g_dis)
# print(dis)
min_d = 0
for index, value in enumerate(dis):
    if value<dis[min_d]:
        min_d = index
# print(min_d)
# print(g[min_d])


namu = bfs(0, ci, cj)
dp = [[0]*m for _ in range(n)]
gost = bfs(1, g[min_d][0], g[min_d][1])
# print(namu)
# print(gost)
if namu!='No' and namu < gost:
    print('Yes')
else:
    print('No')
