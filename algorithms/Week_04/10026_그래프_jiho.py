# 적록색약
"""
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
from collections import deque

def dfs(s, ci, cj):
    dp[ci][cj] = 1
    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == s and dp[ni][nj] == 0:
            dfs(s, ni, nj)
    return 1
N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

# 갔다는 것 저장
dp = [[0]*N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            s = arr[i][j]
            cnt += dfs(s, i, j)
# print(cnt, end=" ")
# rb_arr = [a[:] for a in arr] ## 이거 꼭 기억하기!!
for i in range(N):
    for j in range(N):
       if arr[i][j] == 'G':
            arr[i][j] = 'R'
dp = [[0]*N for _ in range(N)]
rb_cnt = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            s = arr[i][j]
            rb_cnt += dfs(s, i, j)
print(cnt, rb_cnt)
"""
### ----- dfs로하니까 메모리 초과 나옴... dfs로 바꾸기

import sys
from sys import stdin
from collections import deque

sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def bfs(s, start_i, start_j):
    queue = deque([(start_i, start_j)])
    dp[start_i][start_j] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == s and dp[ni][nj] == 0:
                dp[ni][nj] = 1
                queue.append((ni, nj))
    return 1

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

# 갔다는 것 저장
dp = [[0] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            s = arr[i][j]
            cnt += bfs(s, i, j)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

dp = [[0] * N for _ in range(N)]
rb_cnt = 0

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            s = arr[i][j]
            rb_cnt += bfs(s, i, j)

print(cnt, rb_cnt)
