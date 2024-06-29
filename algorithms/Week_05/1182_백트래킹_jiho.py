# 부분 수열의 합
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, a):
    global ans
    if n==N:
        # print(a)
        if len(a) != 0 and sum(a) == S:
            # print(a)
            ans +=1
        return
    dfs(n+1, a + [arr[n]]) # 포함하는 경우
    dfs(n+1, a) # 포함하지 않는 경우

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
dfs(0, [])
print(ans)