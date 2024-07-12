# 타일 채우기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())

if n%2!=0: # n이 홀수이면
    print(0)
else: # n이 짝수이면
    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = 3 # 처음 n=2일땐 3개 초기화
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*3 # 기본 패턴 (3개에 3개씩이 더 곱해짐)
        for j in range(4, i+1, 2):
            # 특수 패턴 추가 -> 이전에 나온 패턴들에서 +2 하기
            dp[i] += dp[i-j]*2

    print(dp[n])