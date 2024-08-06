# 알고스팟 => bfs(appendleft 기억하기!!), 다 익스트라
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(i,j):
    q = deque()
    q.append((i,j))
    dp = [[-1]*M for _ in range(N)] # 벽 개수 저장
    dp[i][j] = 0 # 첫번째 벽 깬걸 0으로 초기화
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and dp[ni][nj]==-1: # 범위내 미방문
                if arr[ni][nj] == 0: # 벽이 아니라면
                    dp[ni][nj] = dp[ci][cj] # 전에 벽을 깬 횟수 그래로 전달
                    q.appendleft((ni, nj)) # 0인것을 우선으로 빼기!!! 이게 중요
                else: # 벽이 라면
                    dp[ni][nj] = dp[ci][cj] + 1 # 벽 횟수 늘리기
                    q.append((ni, nj))

    # for i in dp:
    #     print(i)
    return dp[-1][-1]

M,N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(0,0))
