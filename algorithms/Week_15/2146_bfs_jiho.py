# 다리 만들기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque , defaultdict

def ans_bfs(lst, k):
    dp = [[-1] * n for _ in range(n)]
    q = deque(lst)
    for i, j in lst:
        dp[i][j] = 0
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n: # 범위내,
                if arr[ni][nj]==0: # 바다일 때
                    if (dp[ni][nj]>dp[ci][cj]+1 and dp[ni][nj] != -1) or dp[ni][nj] == -1:
                        dp[ni][nj] = dp[ci][cj] + 1
                        q.append((ni, nj))
    ans = 100*100+1
    for key, value in island.items():
        if key == k: continue
        # print(key, value)

        q = deque(value)
        while q:
            ci, cj = q.popleft()
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<n and 0<=nj<n and dp[ni][nj]!=-1: # 범위내
                    # print(dp[ni][nj])
                    ans = min(ans, dp[ni][nj])

    # print()
    # for i in dp:
    #     print(i)
    # print("ans: ", ans)
    return ans

def split_bfs(i,j, idx):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    arr[i][j] = idx
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = True
                arr[ni][nj] = idx
                q.append((ni,nj))

n = int(input())
visited = [[False]*n for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]


# 섬 구분
idx = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            split_bfs(i,j, idx)
            idx +=1

island = defaultdict(list) # 각 섬의 좌표 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] !=0:
            island[arr[i][j]].append((i,j))
# for key, value in island.items():
#     print(key)
anss = 100*100+1
for key, value in island.items():
    anss = min(anss, ans_bfs(value, key))
print(anss)