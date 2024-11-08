# 숨바꼭질 4
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
# 딕셔너리 사용
# INF = sys.maxsize
def bfs(n):
    q = deque([n])
    dp[n] = n
    # move = [n]
    while q:
        ci = q.popleft()
        if ci==K:
            return ci
        for ni in (ci*2, ci-1, ci+1):
            if 0<=ni<=100000 and ni not in dp:
                dp[ni] = ci
                q.append(ni)
                # move.append(ni)


N, K = map(int, input().split())
dp = dict()
c = bfs(N)
ans = deque()
cnt = 0
# print(dp)
while dp[c]!=c:
    ans.appendleft(c)
    c = dp[c]
    cnt+=1
ans.appendleft(c)
print(cnt)
print(*ans)


