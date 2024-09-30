# 로봇 조종하기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = 0
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF]*M for _ in range(N)] # 최대값 저장
tmp = [[INF]*M for _ in range(2)] # 왼쪽 -> / 오른쪽 <-

# DP의 0번째 행렬 초기화
dp[0][0] = arr[0][0]
for j in range(1,M):
    dp[0][j] = dp[0][j-1]+arr[0][j]
# print(dp)

# 나머지 DP행에 대해서 최대값 구하기
for i in range(1,N):
    # 왼쪽 부터 시작
    for j in range(M):
        if j==0:
            tmp[0][j] = dp[i-1][j]+arr[i][j]
        else:
            tmp[0][j] = max(dp[i-1][j], tmp[0][j-1])+arr[i][j]
    # 오른쪽 부터 시작
    for j in range(M-1, -1, -1):
        if j==M-1:
            tmp[1][j] = dp[i-1][j]+arr[i][j]
        else:
            tmp[1][j] = max(dp[i - 1][j], tmp[1][j + 1]) + arr[i][j]
    # print(tmp)
    dp[i] = list(map(max, *tmp))
    # print(dp)
print(dp[-1][-1])
