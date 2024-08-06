# 미로만들기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v = [[-1]*n for _ in range(n)] # 검은방 바꿀 수 저장 & 아직 미방문은 -1
    v[i][j] = 0 # 처음에 0개 시작
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == -1: # 범위내, 미방문
                if arr[ni][nj]==1: # 흰방이면 먼저 들어가기
                    v[ni][nj] = v[ci][cj] # 기존꺼 넣기
                    q.appendleft((ni,nj))
                else: # 검은방이면
                    v[ni][nj] = v[ci][cj] +1
                    q.append((ni,nj))
    return v[-1][-1]

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0,0))