# 벽 부수고 이동하기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j,f):
    q = deque()
    q.append((i,j,f))

    while(q): # q가 있을때까지 반복
        ci, cj, cf = q.popleft()
        # 끝점 도달 시 이동 횟수 return
        if ci==n-1 and cj==m-1:
            return visited[ci][cj][cf]

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m: # 범위 내
                # 이동할 곳이 벽이 아니고, 방문 전
                if arr[ni][nj] == 0 and visited[ni][nj][cf] == 0: # 방문 전이면
                    visited[ni][nj][cf] = visited[ci][cj][cf] + 1
                    q.append((ni,nj,cf))
                # 이동할 곳이 벽이고, 벽 뿌수기 전이라면
                elif arr[ni][nj] == 1 and cf == 0: # 벽 안뿌셨으면
                    visited[ni][nj][1] = visited[ci][cj][0] + 1
                    q.append((ni, nj, 1)) # 벽 부숨

    return -1


n,m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# 상, 하, 좌, 우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs(0,0,0))
