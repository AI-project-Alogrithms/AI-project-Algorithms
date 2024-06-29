# GBC level 2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
arr = [0]*101
cur = 1
# 모든 구간별 speed를 저장해둠
for _ in range(N):
    a, speed = map(int, input().split())
    for i in range(cur, cur+a):
        arr[i] = speed
    cur += a

ans = 0
cur = 1
for _ in range(M):
    a, speed = map(int, input().split())
    for i in range(cur, cur+a):
        ans = max(ans, speed - arr[i])
    cur += a
print(ans)
