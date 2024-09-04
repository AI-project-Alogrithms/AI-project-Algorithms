# 상범빌딩
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(sk, si, sj):
    q = deque()
    q.append((sk, si, sj))
    dp[sk][si][sj] = 1
    while q:
        ck, ci, cj = q.popleft()
        for d in range(6):
            nk, ni, nj = ck + dz[d], ci + dx[d], cj + dy[d]
            if 0<=nk<l and 0<=ni<r and 0<=nj<c: # 범위내
                if arr[nk][ni][nj] == 'E': # 탈출?
                    print("Escaped in {} minute(s).".format(dp[ck][ci][cj]))
                    return
                if arr[nk][ni][nj] == '.' and dp[nk][ni][nj] == -1:
                    dp[nk][ni][nj] = dp[ck][ci][cj] + 1
                    q.append((nk, ni, nj))
    print("Trapped!")

while(True):
    l, r, c = map(int, input().split())
    if l==0 and r==0 and c==0: break
    arr = [[[]*c for _ in range(r)] for _ in range(l)]
    dp = [[[-1]*(c) for _ in range(r)] for _ in range(l)]
    # arr.append(tr)
    for i in range(l):
        arr[i] = [list(input().rstrip()) for _ in range(r)]
        input()
    # arr[layer][row][column]
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if arr[k][i][j] == 'S':
                    bfs(k, i, j)
