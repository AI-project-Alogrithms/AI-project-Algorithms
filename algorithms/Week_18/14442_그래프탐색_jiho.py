# 벽 부수고 이동하기 2
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = 10**9
from collections import deque
def bfs():
    q = deque()
    q.append([0,0,k])
    dp[0][0][k] = 1 # 방문 여부

    while q:
        ci, cj, ck = q.popleft()
        # # 끝점 도달 시 이동 횟수 return
        if ci==N-1 and cj==M-1:
            return dp[ci][cj][ck]

        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                # 벽이 아니면, 방문 전
                if arr[ni][nj] == 0 and dp[ni][nj][ck]==0:
                    dp[ni][nj][ck] = dp[ci][cj][ck]+1
                    q.append((ni,nj,ck)) # 벽 아닌 거 -> 그 다음이동도 벽 아닌거
                elif arr[ni][nj]==1 and ck>0 and dp[ni][nj][ck-1] == 0: # 벽이고, 아직 부수기 전이고, 개수가 남아있다면
                    dp[ni][nj][ck-1] = dp[ci][cj][ck] +1
                    q.append((ni,nj,ck-1))
    # for i in dp:
    #     print(i)
    return -1

N, M, k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [[[0]*(k+1) for _ in range(M)] for _ in range(N)] # 벽 파괴 가능, 불가능, 파괴 개수
# v = [[0]*M for _ in range(N)]
print(bfs())
# print(ans+1 if ans!= INF else -1)