import sys

# sys.stdin = open('/content/input.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and v[ni][nj] == -1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    for i, j in empty:
        v[i][j] = 0
    for i in v:
        print(" ".join(map(str, i)))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
empty = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            ci, cj = i, j
# print(empty)
v = [[-1] * m for _ in range(n)]
bfs(ci, cj)
