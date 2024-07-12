# 동전 2: 점화식은 만들었는데 더 복잡하게 식을 썼다. 초기화를 inf로 안한게 함정..
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution(dp):
    for i in range(1,n+1):
        for j in range(1,k+1):
            if value[i] <= j:
                dp[j] = min(dp[j], dp[j - value[i]] + 1)
    # print(dp)
            # if i==1 and j%value[i]==0:
            #     dp[i][j] = int(j//value[i])
            # else:
            #     if value[i] > j:
            #         dp[i][j] = dp[i-1][j]
            #     else:
            #         # print(dp)
            #         if j%value[i]==0:
            #             dp[i][j] = min(dp[i-1][j], dp[i][j-value[i]]+1)
            #         else:
            #             dp[i][j] = dp[i - 1][j]
    # print(dp)
    if dp[k] == 10001:
        return -1
    else:
        return dp[k]

n, k = map(int, input().split())
value = []
for _ in range(n):
    value.append(int(input()))
value = [0] + value
value.sort()
dp = [10001] * (k + 1)
dp[0] = 0
print(solution(dp))
