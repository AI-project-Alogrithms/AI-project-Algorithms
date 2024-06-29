# 알파벳
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# from collections import deque

def dfs(cnt, ci,cj,visited):
    global max_v
    max_v = max(max_v, cnt)
     # 돌 방향이 몇개인지
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<r and 0<= nj<c and not visited[ord(arr[ni][nj])-ord('A')]: # 해당 알파벳을 방문한 적이 없다면
            visited[ord(arr[ni][nj])-ord('A')] = True
            dfs(cnt+1, ni, nj, visited)
            visited[ord(arr[ni][nj]) - ord('A')] = False

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

# 알파벳을 사용했는지 안했는지 확인 0~26까지 A~Z변환
visited = [False] * 26
visited[ord(arr[0][0])-ord('A')] = True

max_v = 0
flag = True
dfs(1,0,0, visited) # CNT, i,j, visited
print(max_v)