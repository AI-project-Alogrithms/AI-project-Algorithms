# 쉬운 최단거리
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(ti, tj):
    q = deque()
    q.append((ti, tj))
    v[ti][tj] = 0
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj]==-1 and arr[ni][nj]==1: # 범위내, 미방문
                # 갈 수 있는 땅이면
                v[ni][nj] = v[ci][cj] +1
                q.append((ni, nj))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and v[i][j] == -1:
                v[i][j] = 0

    return v




# 각 지점에서 목표지점까지의 거리 출력
n,m = map(int, input().split())
# 0: 갈수없는 땅, 갈수있는 땅 부분 중 도달할 수 없는 위치 -1
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            ti, tj = i,j # 목표 지점

v = [[-1]*m for _ in range(n)]
visited = bfs(ti, tj)
for i in visited:
    print(" ".join(map(str, i)))