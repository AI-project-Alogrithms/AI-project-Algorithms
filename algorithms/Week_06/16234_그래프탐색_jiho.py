# 인구 이동
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(arr, x, y, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 # 해당 나라는 방문
    add_lst = [(x,y)]
    total_num = arr[x][y]
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and L<= abs(arr[ci][cj] - arr[ni][nj]) <= R and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                add_lst.append((ni,nj)) # 좌표 저장 -> 해당 좌표 값 변경 위해서
                total_num += arr[ni][nj]
                q.append((ni, nj))
    return add_lst, total_num

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while(True):
    visited = [[0] * N for _ in range(N)]
    total_add_lst = []
    move = False
    # 각 나라마다 인구 이동이 있는지 확인
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 방문 안한 곳이라면
                add_lst, total_num = bfs(arr,i,j,visited)
                if len(add_lst) > 1: # 연결된 나라가 있다면
                    move = True
                new_num = total_num//len(add_lst)
                for x, y in add_lst:
                    arr[x][y] = new_num
    if not move:
        break # 방문한 곳이 없다면

    cnt +=1
print(cnt)
