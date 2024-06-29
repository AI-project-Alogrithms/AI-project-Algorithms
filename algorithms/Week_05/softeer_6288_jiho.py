# 금고털이 level2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

w, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda x: x[1], reverse=True)
# print(arr)
value = 0
for i in range(n):
    if w == 0:
        break
    if w >= arr[i][0]:
        w-= arr[i][0]
        value += arr[i][0] * arr[i][1]
    else: # w가 i보다 작으면
        value += w * arr[i][1]
        w = 0
print(value)