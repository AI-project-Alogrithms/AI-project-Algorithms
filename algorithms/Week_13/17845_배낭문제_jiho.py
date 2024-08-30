import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def func():
    for i in range(1,K+1):
        for j in range(10001):
            if lst[i][1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][1]]+lst[i][0])

    print(dp[K][N])

N, K= map(int, input().split())
lst = [[0,0]] + [list(map(int, input().split())) for _ in range(K)]
# print(lst)

dp = [[0]*(10001) for _ in range(K+1)]
# print(dp)
func()