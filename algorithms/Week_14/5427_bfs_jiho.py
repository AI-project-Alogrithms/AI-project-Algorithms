# 불
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs():

    while fire_q:
        ci, cj, t = fire_q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if ni<0 or ni >= h or nj <0 or nj >= w: continue
            # 벽이 아니고, 방문하지 않았다면
            if arr[ni][nj] != '#' and dp[ni][nj]==0:
                dp[ni][nj] = t+1 # 숫자 세기
                fire_q.append((ni,nj,t+1))

    while person_q:
        ci, cj, ct = person_q.popleft()
        # 탈출했다면 (제일 끝까지 왔다면)
        if ci==h-1 or ci==0 or cj==w-1 or cj==0:
            return ct
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if ni<0 or ni >= h or nj <0 or nj >= w: continue
            if arr[ni][nj] !='#': # 벽이 아니고, 불 붙기 전 이동가능하거나, 아직 불이 붙지 않은 곳이라면
                if ct+1 < dp[ni][nj] and dp[ni][nj] != -1 or dp[ni][nj] ==0 :
                    person_q.append((ni,nj,ct+1))
                    dp[ni][nj]=-1
    return "IMPOSSIBLE"

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    fire_q = deque() # 불의 이동 먼저 처리
    person_q = deque() # 사람의 이동 처리
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_q.append((i,j,1))
                dp[i][j] = 1 # 방문 세기
            elif arr[i][j] == '@':
                person_q.append((i,j,1)) # 이동거리를 함께 저장
#     print(q)
    print(bfs())

