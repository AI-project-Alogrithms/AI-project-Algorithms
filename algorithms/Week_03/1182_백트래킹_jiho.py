# 부분 수열의 합
import sys
from sys import stdin

# from collections import deque

# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def dfs(num, sm, cnt):
    global ans
    if num == n:
        if sm==s and cnt > 0:
            ans +=1
        return
    # 하부 함수 호출
    dfs(num+1, sm+lst[num], cnt+1) # 포함하는 경우
    dfs(num+1, sm, cnt) # 포함하지 않은 경우
n,s = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0

dfs(0, 0, 0)
print(ans)