# 택배 배송
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = 10**9
def dijkstra(node):
    q = []
    heapq.heappush(q, (0, node)) # 현재 거리, 현재 위치
    distance[node] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for next_node, cow in arr[now]:
            cost = cow+dist
            if cost<distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    print(distance[N])

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))
distance = [INF]*(N+1)
dijkstra(1)

