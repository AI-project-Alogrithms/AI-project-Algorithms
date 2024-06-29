# 동계 테스트 시점 예측 = 백준 2638 치즈
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def check():
    for i in range(N):
        if sum(arr[i]):
            return True
    return False

def remove_water():
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1 # 다시 원상 복구
    return

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True # 방문 표시
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]: # 범위내, 미방문
                if arr[ni][nj] == 0: # 0이면
                    q.append((ni, nj)) # 바깥에 있는 0 다 탐색 (연결되어 있는)
                    visited[ni][nj] = True
                else: # 1이면
                    arr[ni][nj] += 1 # 0에 접해있는 빙하라는 표시 하기
    # 3이상인 숫자 제거 (원래가 1이니까 두번 터치시 3)
    remove_water()
    return arr


N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


time = 0
while(check()):
    # 전체가 다 0이되면 break
    arr = bfs(0,0)
    time +=1
print(time)
