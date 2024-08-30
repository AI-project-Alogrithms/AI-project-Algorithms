import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
sys.setrecursionlimit(10000)  # 재귀 한도를 늘리기
input = sys.stdin.readline
# from collections import deque
def dfs(ci,cj):

    if dp[ci][cj] != -1: # 이미 계산된 경우
        return dp[ci][cj] # 반환

    # eat = arr[ci][cj] # 초기값
    dp[ci][cj] = 1
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<n and 0<=nj<n and arr[ci][cj]<arr[ni][nj]:
            dp[ci][cj] = max(dp[ci][cj], dfs(ni,nj)+1) # dfs로 들어갔을 때 최댓값과 현재 최댓값 중 max 저장
    return dp[ci][cj]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)] # 이동할 수 있는 최대 칸 수 저장 (해당 지점에서 시작했을 때)
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)