# 암호코드
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

lst = list(map(int, input().rstrip()))
dp = [0]*(len(lst)+1)
dp[0] = 1
dp[1] = 1 # 첫번째 자리

if lst[0]==0: # 첫번재 자리가 0이면 해석할 수 없음
    print(0)
else:
    for k in range(1,len(lst)):
        i = k+1
        if lst[k] > 0: # 1자리 가능
            dp[i] += dp[i-1]
        if 10<= lst[k-1]*10 + lst[k] <= 26: # 2자리 가능
            dp[i] += dp[i-2]
    print(dp[-1]%1000000)
