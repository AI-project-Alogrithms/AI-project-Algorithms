# 내리막길 ㅉ
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

di = [0,0,-1,1]
dj = [1,-1,0,0]

def dfs(i, j):
    if dp[i][j] == -1: # 메모이제이션 처리
        dp[i][j]=0 # 방문 표시
        for d in range(4):
            pi, pj = i+di[d], j+dj[d]
            if 0<=pi<m and 0<=pj<n and arr[pi][pj]>arr[i][j]:
                    dp[i][j]+=dfs(pi,pj)

    return dp[i][j]

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans = 0
dp = [[-1]*n for _ in range(m)]
dp[0][0] = 1
# dp[m-1][n-1] = 1
print(dfs(m-1, n-1))

