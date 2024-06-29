# N과 M
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, ans, dp):
    if n == M:
        for i in dp:
            if set(ans) in dp:  # 이미 있다면
                return

        dp.append(set(ans))
        # print("dp: ", dp)
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        if i in ans: continue
        dfs(n+1, ans+[i], dp)
N, M = map(int, input().split())
# dp = []
dfs(0, [], [])