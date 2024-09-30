# 여행
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def dfs(c, node):
    global ans
    if c>M: # 간선 수가 M을 초과하면 리턴
        return -float('inf')
    if dp[node][c] != -1: # 이미 계산된 상태면 바로 리턴
        return dp[node][c]
    if node==N: # 도착 노드에 도달하면 리턴
        return 0 # 더이상 갈 필요 없으므로 0
    max_cost = -float('inf')
    for next, value in graph[node]:
        if next>node:
            max_cost = max(max_cost, dfs(c+1, next)+value)
    dp[node][c] = max_cost
    return dp[node][c]



N, M, K = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
dp = [[-1]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
visited[1] = 1
# print(graph)
# dijkstra()
ans = dfs(1,1)
print(ans if ans!= -float('inf') else 0)
# print(ans)