# 장애물 인식 프로그램
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1 # 방문
    count = 1 # 블록 개수
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                v[ni][nj] = 1
                count +=1
                q.append((ni,nj))

    return count

N = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(N)]
v = [[0]*N for _ in range(N)] # 방문 여부
cnt = 0 # 블록 개수
lst = [] # 블록 수
for i in range(N):
    for j in range(N):
        # 미방문, 장애물
        if v[i][j]==0 and arr[i][j]==1:
            lst.append(bfs(i,j))
            cnt +=1 # 블록 개수 더하기
print(cnt)
lst.sort()
print("\n".join(map(str, lst)))
