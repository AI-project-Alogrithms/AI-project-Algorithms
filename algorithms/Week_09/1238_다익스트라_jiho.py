# 파티
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start)) # dist, now
    distance[start] = 0 # 자기자신으로 가는거 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    # print(distance)
    return distance

# X:파티 참석 마을
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t)) # end, time
# print(graph)
# X에서 각 N명의 학생들의 도시로 가는데 최소 시간
go_distance = dijkstra(X, distance)
# print(go_distance)
# 각 도시에서 X로 가는데 최소시간
lst = [INF]*(N+1)
for i in range(1,N+1):
    distance = [INF] * (N + 1)
    back_distance = dijkstra(i, distance)
    lst[i] = back_distance[X]
# print(lst)
sum = [x+y for x,y in zip(go_distance[1:], lst[1:])]
print(max(sum))
