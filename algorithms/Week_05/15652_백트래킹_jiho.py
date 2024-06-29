# N과 M
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
def dfs(start, ans):
    if len(ans)==M:
        # print("ans", end = " ")
        print(" ".join(map(str, ans)))
        return
    # print("start: ", start)
    for i in range(start, N+1):
        # print("i: ", i )
        dfs(i, ans+[i])

N, M = map(int, input().split())
dfs(1, []) # START, [] ANS