# 보물섬
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))

    clst = [[0]*(m) for _ in range(n)]
    clst[i][j] = 1
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni<n and 0<= nj < m and arr[ni][nj] == 'L' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                clst[ni][nj] = clst[ci][cj] +1
                q.append((ni, nj))
    # print(max(map(max, *clst)))
    return max(map(max, *clst))-1

n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(n)]
# print(arr)
visited = [[0]*(m) for _ in range(n)]
saved =  [[0]*(m) for _ in range(n)]
max_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L' and visited[i][j] == 0 and saved[i][j] == 0:
            visited[i][j] = 1
            c = bfs(i,j)
            # max_cnt = max(max_cnt, c)
            # 각 위치마다의 최단거리 탐색을 위해 visited는 초기화, 대신 각 위치에서의 최단 거리 저장 배열 한개 더 만들기
            visited = [[0] * (m) for _ in range(n)]
            saved[i][j] = c
# print(max_cnt)
print(max(map(max, *saved)))