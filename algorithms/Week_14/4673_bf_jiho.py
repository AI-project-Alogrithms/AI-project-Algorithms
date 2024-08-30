# 셀프 넘버
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def d(n):
    # if len(n)==1:
    #     t = n+n
    # else:
    t = n
    for s in str(t):
        t+=int(s)
    if t <=10000 and dp[t]==0:
        dp[t]=1

dp = [0]*10001
for i in range(1,10001):
    d(i)

for i in range(1,10001):
    if dp[i]==0:
        print(i)