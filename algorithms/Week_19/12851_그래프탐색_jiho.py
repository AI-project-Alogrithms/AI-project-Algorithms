# 숨바꼭질 2
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
INF = 10**9+1

def bfs(n):
    q = deque([n])
    dp[n] = 0  # 시간

    ans, cnt = 0,0
    while q:
        cur = q.popleft()
        if cur == K:
            # ans = dp[n][0]
            cnt +=1
            continue
        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= 100000:
                if (dp[next] >= dp[cur] + 1):
                    dp[next] = dp[cur] + 1
                    q.append(next)
    print(dp[K])
    print(cnt)


N, K = map(int, input().split())
dp = [INF for _ in range(100001)]  # dp 배열 크기를 100001로 제한
bfs(N)