# 평범한 배낭 -> 현대오토 문제와 유사
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]

# 초기화 위해서 0행 추가
dp = [[0]*(K+1) for _ in range(N+1)]
# print(bag)

for i in range(1,N+1): # 물품 수 만큼 돌동안
    for j in range(1,K+1): # 넣을 수 있는 무게 나열
        # print(dp)
        if j >= bag[i-1][0]: # 넣을 수 있는 무게가 해당 물건 무게보다 크다면
            # print("dp[i-1][j]: ", dp[i-1][j])
            # print("이게 무슨 값이냐: ",dp[i-1][j-bag[i-1][0]])
            dp[i][j] = max(dp[i-1][j], bag[i-1][1]+dp[i-1][j-bag[i-1][0]])
        else:
            # 현재최대무게j가 해당 물건 무게보다 작다면 (담을 수 없음)
            dp[i][j] = dp[i-1][j]
print(dp[N][K])