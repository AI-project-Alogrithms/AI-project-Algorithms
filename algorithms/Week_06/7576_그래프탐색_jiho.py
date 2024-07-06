# 토마토 => bfs 탐색, 동시에 익어야 되니까 토마도 위치를 미리 다 큐에 넣어두기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(tomato):
    q = deque(tomato)
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni<N and 0<= nj<M and arr[ni][nj] == 0:
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni,nj))
    return arr

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tomato = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i,j))

arr = bfs(tomato)
arr_sum = sum(arr,[])
if 0 in arr_sum:
    print(-1)
else:
    print(max(arr_sum)-1)

