# 로또
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, ans, start):
    if n==6:
        print(" ".join(map(str, ans)))
        return
    # i = 0
    for i in range(start, N):
        if lst[i] in ans: continue
        dfs(n+1, ans + [lst[i]], i+1) # 이전에 선택한 요소 이후부터 선택
    # i += 1




while(True):
    lst = list(map(int, input().split()))
    N = lst[0]
    lst = lst[1:]
    lst.sort()
    if N == 0:
        break
    dfs(0, [], 0)
    print()
