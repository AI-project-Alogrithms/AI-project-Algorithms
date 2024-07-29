# 최소비용구하기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #(dist, now)
    distance[start] = 0 # 초기 거리 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost<distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,c = map(int, input().split())
    graph[s].append((e,c))
distance = [INF]*(N+1)
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])