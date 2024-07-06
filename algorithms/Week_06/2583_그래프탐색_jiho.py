# 영역 구하기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(ci, cj):
    cnt = 1
    q = deque()
    q.append((ci, cj))
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cnt +=1
                q.append((ni, nj))

    return cnt

# 열, 행, 직사각형 개수
M, N, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for _ in range(K):
    a,c,b,d  = map(int, input().split())
    for i in range(a,b):
        for j in range(c,d):
            arr[i][j] = -1
# print(arr)

visited = [[0]*M for _ in range(N)]
ans = 0
ans_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = bfs(i,j)
            ans_lst.append(cnt)
ans_lst.sort()
print(len(ans_lst))
print(" ".join(map(str, ans_lst)))


