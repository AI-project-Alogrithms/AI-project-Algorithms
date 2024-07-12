# 상자넣기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# print(arr)
# dp 배열 초기화
dp = [1] * (n)

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]: #
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

