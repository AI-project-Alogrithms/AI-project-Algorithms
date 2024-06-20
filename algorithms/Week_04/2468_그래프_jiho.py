# 안전영역
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(x,y, dp):
    q = deque()
    q.append((x,y))
    dp[x][y] = 1
    while(q):
        x, y = q.popleft()
        for r, c in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = x+r, y+c
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] > h and dp[nx][ny] == 0:
                dp[nx][ny] = 1
                q.append((nx, ny))
    return 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_h = 0 # 가장 max값이 마지노선
for i in arr:
    max_h = max(max_h,max(i))
# print(max_h)
h = 0 # h 최솟값
all_result = []
while(h<=max_h+1):
    result = 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and dp[i][j] ==0 :
                result += bfs(i, j, dp)
    all_result.append(result)
    h+=1
print(max(all_result))
