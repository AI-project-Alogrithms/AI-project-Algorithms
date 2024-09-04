# 말이 되고픈 원숭이 => 3차원 BFS 문제
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
INF = 9876543210

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(i,j,k):
    q = deque()
    q.append((i,j,k))
    dist[0][0][k] = 0 # 현재 최소 거리
    v[i][j][k] = 1 # 방문 표시
    while(q):
        ci, cj, ck = q.popleft()
        # 네방향 거리 확인, 더 최소로 넣기
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < H and 0 <= nj < W and v[ni][nj][ck] == 0 and arr[ni][nj] == 0:
                # 범위내, 미방문, 장애물 없다면
                v[ni][nj][ck] = 1 # 방문 표시
                # 기존 있던 것과 현재 방문에서 가는 것 중 최소 거리로 업데이트
                dist[ni][nj][ck] = min(dist[ni][nj][ck], dist[ci][cj][ck]+1)
                q.append((ni,nj,ck))
        # 말이라면
        if ck>0:
            for d in range(8):
                ni, nj = ci+dx[d], cj+dy[d]
                if 0<=ni<H and 0<=nj<W and v[ni][nj][ck-1]==0 and arr[ni][nj]==0:
                    v[ni][nj][ck-1] = 1
                    dist[ni][nj][ck-1] = min(dist[ni][nj][ck-1], dist[ci][cj][ck]+1)
                    q.append((ni,nj,ck-1))
    return min(dist[-1][-1])





k = int(input())
W, H = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(H)]
dist = [[[INF for _ in range(k+1)] for _ in range(W)] for _ in range(H)]
v = [[[0 for _ in range(k+1)] for _ in range(W)] for _ in range(H)]


ans = bfs(0,0,k)
print(-1 if ans==INF else ans)