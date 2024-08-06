# 주난의 난
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque([(i,j)])
    v=[[-1]*M for _ in range(N)]
    v[i][j] = 0
    while(q):
        ci, cj = q.popleft()
        if arr[ci][cj]=='#': # 범인이면 return
            return v[ci][cj]
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==-1:
                if arr[ni][nj]=='0':
                    v[ni][nj] = v[ci][cj]
                    q.appendleft((ni,nj))
                else:  # 범인이거나, 친구가 있다면 +1
                    v[ni][nj] = v[ci][cj] +1
                    q.append((ni,nj))

N, M = map(int, input().split())
ci, cj, ei, ej = map(int, input().split()) # 주난의 위치, 범인의 위치
arr = [list(input().rstrip()) for _ in range(N)]
# 0: 빈공간, 1: 친구, * 주난, # 범인
print(bfs(ci-1, cj-1))
