# 나무조경.. 맞았음ㅠㅠㅠㅠ다행임...하 level 3
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# import time
# from collections import deque
# start = time.time()
def dfs(n, ans):
    global max_v
    if n==max_N:
        max_v = max(max_v, ans)

        return
    for ci in range(N):
        for cj in range(N):
            if not visited[ci][cj]: # 현재 위치 방문 안했다면
                visited[ci][cj] = True # 현재 위치 방문 표시
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)): # 다음 위치 찾기
                    ni, nj = ci+di, cj+dj
                    if 0<= ni< N and 0<= nj < N and not visited[ni][nj]: # 인접한 다음 위치에 VISIT을 안했다면 방문 하고 현재 + NEXT 값 ANS에 넣기
                        visited[ni][nj] = True
                        dfs(n+1, ans+arr[ci][cj]+arr[ni][nj])
                        visited[ni][nj] = False # NEXT값만 다시 미방문 표시
                visited[ci][cj] = False # 현재 위치 방문 표시 제거하기 이때 TRUE 위치와 동일한 위치에서 제거하는게 핵심임!! 헷갈리지 말기

N = int(input())
arr = []
visited = [[False for _ in range(N)] for _ in range(N)]
result = 0

for _ in range(N):
    arr.append(list(map(int, input().split())))
if N==2:
    max_N = 2
else:
    max_N = 4
max_v = 0
dfs(0, 0)
print(max_v)

# 종료시간
# end = time.time()
# print(end - start)
