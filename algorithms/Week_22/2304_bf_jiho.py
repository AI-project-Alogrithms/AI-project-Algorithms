import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key = lambda x: x[0])
# print(lst)
max_idx = 0
for i in range(n):
    if lst[max_idx][1]<lst[i][1]:
        max_idx = i
# print(max_idx)
ans = lst[max_idx][1]
# 가장 높은 기둥 전까지 왼쪽 부분 면적 더하기
height = lst[0][1]
for i in range(max_idx):
    if height<lst[i+1][1]:
        ans+= height*(lst[i+1][0]-lst[i][0])
        height = lst[i+1][1]
    else:
        ans+= height*(lst[i+1][0] - lst[i][0])
# 오른쪽 부분도 진행
height = lst[-1][1]
for i in range(n-1, max_idx, -1):
    if height<lst[i-1][1]:
        ans+=height*(lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else:
        ans+= height*(lst[i][0]-lst[i-1][0])

print(ans)