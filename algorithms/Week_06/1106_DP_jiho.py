# 호텔 -> 0-1배낭문제, dp값이 최소 비용이 되도록 갱신
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

C, N = map(int, input().split())
lst = [[0,0]]
for _ in range(N):
    value, cus = map(int, input().split())
    lst.append([value, cus])

maxc = float('INF') # MAX COST값이 정해지지 않음 -> 따라서 무한대로 보내기
dp = [[maxc]*(C+1) for _ in range(N+1)]

for i in range(1,N+1):
    value, cus = lst[i][0], lst[i][1]
    # print(value, cus)
    for j in range(1,C+1): # 모든 도시에 대하여 1부터 C까지 이중 반복문을 실행
        dp[i][j] = dp[i-1][j]
        k=0
        while(True): # k의 값을 1씩 늘려가며 현재 도시를 가능한 여러 번 선택한 경우를 모두 탐색
            if j-(k*cus)<=0: # 갱신, 무한 루프 중단
                dp[i][j] = min(dp[i][j], k*value)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-k*cus] + k*value)
            k+=1

print(dp[N][-1])
# print(dp)
