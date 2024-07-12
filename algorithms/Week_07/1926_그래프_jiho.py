# 그림 => bfs, dfs
## ?? bfs 시간 초과...왜지? max_lst를 리스트로 안만들고 그냥 하니까 해결됨
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
def bfs(ci, cj):
    q = deque()
    q.append((ci, cj))
    # dp = [[0] * (m) for _ in range(n)]
    # dp[ci][cj] = 1
    count = 1
    visited[ci][cj] = 1
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and visited[ni][nj] == 0:
                # dp[ni][nj] = dp[ci][cj] + 1
                visited[ni][nj] = 1
                count +=1
                q.append((ni,nj))
    # print(dp)
    return count



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]
max_lst = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and visited[i][j] == 0:
            max_lst = max(max_lst, bfs(i,j))
            cnt +=1
print(cnt)
print(max_lst)