# 게임 0-1 그래프 탐색
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque([(i,j)])
    v = [[-1]*501 for _ in range(501)] # 방문 여부 및 생명 감소 count
    v[i][j] = 0
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < 501 and 0<=nj<501 and v[ni][nj]==-1 and arr[ni][nj]!=2: # 범위내, 미방문, 죽음 구역이 아니라면
                if arr[ni][nj] ==0: # 안전구역이라면
                    v[ni][nj] = v[ci][cj]
                    q.appendleft((ni,nj))
                else:
                    v[ni][nj] = v[ci][cj]+1
                    q.append((ni,nj))
    return v[-1][-1]


# 0 안전, 1 위험, 2 죽음
# 죽음 +위험 = 죽음, 위험 + 안전 = 위험, 위험 + 위험 = 위험, 죽음 + 안전 = 죽음
arr = [[0]*501 for _ in range(501)]
danger = []
death =[]
N = int(input()) # 위험구역의 수
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split()) # 위험 구역의 정보
    danger.append((x1, y1, x2, y2 ))

M = int(input()) # 죽음 구역의 수
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split()) # 죽음 구역의 정보
    death.append((x1, y1, x2, y2))

for i in range(501):
    for j in range(501):
        # 위험 구역이라면 1, 죽음 구역이라면 2
        for a1, b1, a2, b2 in danger:
            if min(a1, a2) <= i <= max(a1, a2) and (min(b1, b2) <= j <= max(b1, b2)):
                arr[i][j] = 1
        for a1, b1, a2, b2 in death:
            if min(a1, a2) <= i <= max(a1, a2) and (min(b1, b2) <= j <= max(b1, b2)):
                arr[i][j] = 2

print(bfs(0,0))
