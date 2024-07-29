# 치즈
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque([(i,j)])
    visited = [[0] * c for _ in range(r)]
    visited[i][j] = 1 # 방문 표시
    lst = [] # 녹을 치즈 위치 저장
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<r and 0<= nj<c and visited[ni][nj] == 0: # 범위내, 미방문
               if arr[ni][nj] == 0:
                   visited[ni][nj] = 1
                   q.append((ni,nj))
               else:
                   # 치즈라면
                   visited[ni][nj] = 1
                   lst.append((ni,nj))
    return lst

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cnt = 0  # 다 녹는데 걸리는 시간
total_sum = sum(map(sum, zip(*arr))) # 초기 치즈 조각 개수
cheeze = [total_sum] # 다 녹기 한시간 전에 남아있는 치즈조각 저장
# print(total_sum)
while(total_sum>0):
    lst = bfs(0,0)  # 치즈가 없는 부분
    for ci, cj in lst:
        arr[ci][cj] = 0
    cnt +=1
    total_sum = sum(map(sum, zip(*arr)))
    if total_sum > 0:
        cheeze.append(total_sum)
print(cnt)
print(cheeze[-1])