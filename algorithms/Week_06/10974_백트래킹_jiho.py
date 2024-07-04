# 모든 순열
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
N = int(input())
def dfs(n, ans):
    if len(ans)==N:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        if i in ans: continue
        dfs(n+1, ans+[i])
dfs(0, [])