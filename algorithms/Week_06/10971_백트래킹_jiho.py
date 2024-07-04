# 외판원 순회2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/O/neDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(start, now, value, cnt):
    global ans
    if cnt==N: # 순회 다했으면
        if arr[now][start] !=0: # 방문 가능하다면
            value += arr[now][start]
            ans = min(ans, value)
        return
    if value > ans:
        return
    for i in range(N):
        if visited[i] == 0 and arr[now][i] !=0: # 현재 위치에서 방문 가능한 곳이 있다면
            visited[i]=1
            dfs(start, i, value+arr[now][i], cnt+1) # 방문, 그 위치를 now로 바꾸기
            visited[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans=1000000*10*10
for i in range(N): # 1~N까지 돌면서
    visited[i] = 1
    dfs(i, i, 0, 1) # 시작 위치 저장 (순회 위해서, now, value, cnt)
    visited[i] = 0

print(ans)