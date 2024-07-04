# n과 m(8)
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(start, ans):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    temp = 0 # 기억할 거
    for i in range(start, N):
        if temp != lst[i]:
            temp = lst[i]
            dfs(i, ans+[lst[i]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dp = []
dfs(0,[])