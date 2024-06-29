# 빙산
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def check(ci,cj):
    count = 0
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        # 상하좌우 보면서 0인 개수 찾기
        ni, nj = ci+di, cj+dj
        if arr[ni][nj] == 0:
            count +=1
    return count

def bfs(ci, cj, dp):
    q = deque()
    q.append((ci, cj))
    dp[ci][cj] = 1
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # 상하좌우 보면서 연결된 거 끼리 표시하기
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] !=0 and dp[ni][nj] == 0:
                dp[ni][nj] = 1
                q.append((ni, nj))
    return 1

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp_arr = [a[:] for a in arr]
year = 0 # 몇년 후?
while(True):
    break_cnt = 0
    dp_arr = [a[:] for a in arr]
    for i in range(1,n-1):
        for j in range(1, m-1):
            if arr[i][j] != 0: # 빙산이라면
                cnt = check(i,j)
                dp_arr[i][j] = max(0,arr[i][j] - cnt) # 음수일 경우 0으로 만들기
            else:
                break_cnt += 1
    year += 1 # 년수 +1
    arr = [a[:] for a in dp_arr]
    dp = [[0]*m for _ in range(n)] # 탐색 유무
    dong = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] !=0 and dp[i][j] == 0: # 아직 탐색 전이고, 빙산이 있다면
                dong += bfs(i, j, dp)
    if dong >= 2:
        print(year)
        break
    else:
        if break_cnt == (n-2)*(m-2): # 모두 0이어도 분리되지 않으면
            print(0)
            break
