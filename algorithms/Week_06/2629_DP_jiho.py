# 양팔저울 --> 백트래킹으로 일단 품..시간초과ㅋㅋ
# dp로 풀기: 중복된 것은 계산하지 않도록 하기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(cnt, w): # 추로 판별할 수 있는 구슬의 무게 전체
    if cnt > N: # 구슬의 숫자가 주어진 구슬보다 크다면 return
        return
    if dp[cnt][w]==1: # 이미 같은 추의 무게와 개수로 방문했다면
        return
    dp[cnt][w] = 1

    dfs(cnt+1, w+weight[cnt-1]) # 추 넣기
    dfs(cnt+1, w)
    dfs(cnt+1, w - weight[cnt-1]) # 무게 빼기


N = int(input())
weight = list(map(int, input().split()))
target_n = int(input())
target = list(map(int, input().split()))
# dp[사용한 추의 개수][추의 무게 차이]
dp = [[0 for _ in range((500*j)+1)] for j in range(N+1)]
ans = []
dfs(0,0)
# print(dp)
for ta in target:
    if ta > 500*N:
        print('N', end = ' ')
    elif dp[N][ta] == 1:
        print('Y', end= ' ')
    else:
        print('N', end = ' ')
"""
# 백트래킹으로 푼거... 첫번째 방식 -> 시간초과

def dfs(n, ta):
    global ans
    if n==N:
        if ta == 0:
            ans = 'Y'
        return
    if ta < 0:
        return
    for i in range(n, N):
        dfs(n+1, ta-weight[i])
        dfs(n + 1, ta + weight[i])
        dfs(n + 1, ta * weight[i])

N = int(input())
weight = list(map(int, input().split()))
target_n = int(input())
target = list(map(int, input().split()))

for i in range(target_n):
    ta = target[i]
    ans = 'N'
    dfs(0, ta)
    print(ans, end=" ")

"""
