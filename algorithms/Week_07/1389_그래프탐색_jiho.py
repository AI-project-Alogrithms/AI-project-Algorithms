# 케빈 베이컨의 6단계 법칙
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(root):
    q=deque(arr[root])
    dp = [0]*(N+1)
    cnt = [1]*(N+1)
    dp[root] = 1
    cnt[root] = 0
    for i in arr[root]:
        dp[i] =1
    while(q):
        node = q.popleft()
        for i in arr[node]:
            if dp[i] == 0: # 방문 전이라면
                cnt[i] += cnt[node]
                dp[i] = 1
                q.append(i)
    # print(cnt)
    return sum(cnt[1:])



N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if (b not in arr[a]) and (a not in arr[b]): # 중복되지 않았으면
        arr[a].append(b)
        arr[b].append(a)
# print(arr)
total = []
for i in range(1,N+1):
    total.append(bfs(i))
print(total.index(min(total))+1)


