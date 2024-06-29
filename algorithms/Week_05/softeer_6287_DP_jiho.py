# 조립라인
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
work = [[],[]] # A, B일하는 시간
swich  = [[],[]]


for _ in range(N-1):
    a,b,ab,ba = map(int, input().split())
    work[0].append(a)
    work[1].append(b)
    swich[0].append(ab)
    swich[1].append(ba)

a,b = map(int, input().split())
work[0].append(a)
work[1].append(b)
dp = [list(0*N for _ in range(N)) for _ in range(2)]
dp[0][0] = work[0][0]
dp[1][0] = work[1][0]

for i in range(1,N):
    dp[0][i] = min(dp[0][i-1], dp[1][i-1]+swich[1][i-1]) + work[0][i]
    dp[1][i] = min(dp[1][i-1], dp[0][i-1]+swich[0][i-1]) + work[1][i]
print(min(dp[0][-1], dp[1][-1]))


