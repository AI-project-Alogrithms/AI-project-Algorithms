# N과 M
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(start, ans):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, N):
        if arr[i] in ans: continue
        dfs(i, ans + [arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0, [])