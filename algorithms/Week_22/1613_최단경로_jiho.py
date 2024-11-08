# 역사
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    dp[a][b] = n
for k in range(1, n+1): # 거쳐가는 노드
    for a in range(1, n+1): # 시작 노드
        for b in range(1, n+1): # 끝 노드
            dp[a][b] = min(dp[a][b], dp[a][k]+dp[k][b])
# for i in dp:
#     print(i)
s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if dp[a][b]==dp[b][a]:
        print(0)
    elif dp[a][b]<dp[b][a]:
        print(-1)
    elif dp[a][b]>dp[b][a]:
        print(1)