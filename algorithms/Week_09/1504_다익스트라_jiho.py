# 특정한 최단 경로
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start)) # dist, now
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return distance

N, E = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 두개의 서로 다른 정점 번호

# print(graph)

one = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

# 1 -> v1 -> v2 -> N
if one[v1] != INF and v1_dist[v2] != INF and v2_dist[N] != INF:
    path1 =  one[v1] + v1_dist[v2] + v2_dist[N]
else:
    path1 = INF

# 1 -> v2 -> v1 -> N
if one[v2] != INF and v2_dist[v1] != INF and v1_dist[N] != INF:
    path2 =  one[v2] + v2_dist[v1] + v1_dist[N]
else:
    path2 = INF

ans = min(path1, path2)
if ans == INF:
    print(-1)
else:
    print(ans)
