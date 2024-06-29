# N과 M
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, ans):
    if n==M:
        # print(ans)
        print(" ".join(map(str, ans)))
        return

    for i in range(1,N+1):
        # ans.append(i)
        if i in ans: continue # 이미 i가 ans에 들어가 있으면 패쓰
        dfs(n+1, ans + [i])
        # dfs(n+1, ans)


N, M = map(int, input().split())
dfs(0, [])