# N과 M
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, arr, start): # 길이
    if n==M:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, N):
        dfs(n+1, arr+[lst[i]], i)

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

dfs(0,[], 0)