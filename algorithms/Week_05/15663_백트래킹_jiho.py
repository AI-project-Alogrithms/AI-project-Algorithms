# N과 M
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(ans):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    start = 0
    for i in range(0, N):
        if not visited[i] and start != arr[i]:
            visited[i] = True # 방문함
            start = arr[i]
            # print("start: ", start)
            dfs(ans+[arr[i]])
            visited[i] = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*N
dfs([])