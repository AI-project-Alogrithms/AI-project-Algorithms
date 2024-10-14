# 공주님을 구해라!
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
INF = 10**9
def bfs(i,j, cnt):
    q = deque()
    q.append((i,j, cnt))
    v[i][j]=0 # 검을 찾지 않은 상태
    result =INF
    while q:
        ci, cj, cnt  = q.popleft()
        if (ci, cj)==(N-1,M-1):
            result = min(cnt, result)
            return result
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==-1 and arr[ni][nj]!=1:
                if arr[ni][nj]==2: # 검을 찾았어
                    result = cnt+1 + (N-1-ni) + (M-1-nj)
                v[ni][nj] = 1 # 방문 함
                q.append((ni,nj,cnt+1))
    return result

N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[-1]*M for _ in range(N)] # 방문 여부
ans = bfs(0,0,0)
if ans>T:
    print("Fail")
else:
    print(ans)
