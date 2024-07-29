# 최단경로
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # dist, now
    distance[start] = 0 # 초기 최단 거리 0으로 세팅
    # visited[start] = True # 현재 방문 true
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist+ j[1] # 현재 최단 거리 + 해당 정점까지 가는데 필요한 cost
            if cost < distance[j[0]]:
                distance[j[0]] = cost # 현재 최단 경로보다 새로운 경로가 더 작다면 update
                # visited[j[0]] = True
                heapq.heappush(q, (cost, j[0]))
    # print(distance)
    for i in range(1,V+1):
        if distance[i]==INF:
            print('INF')
        else:
            print(distance[i])


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)] # 1~V까지 정점이 있음
K = int(input()) # 시작 정점 번호
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v, w)) # end, cost
# print(graph)
distance = [INF] * (V+1) # 초기 최단 거리 INF
# visited = [False] * (V+1)
dijkstra(K)

