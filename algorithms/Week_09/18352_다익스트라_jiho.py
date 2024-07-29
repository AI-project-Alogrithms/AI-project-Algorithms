# 특정거리의 도시 찾기: bfs, 다익스트라 알고리즘
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
import heapq # 다익스트라 알고리즘 때 활용
INF = int(1e9) # 무한대

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue # 현재 최단 거리보다 지금 최단 거리가 크다면
        for j in graph[now]:
            cost = dist+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append((b,1)) # 각 에지의 가중치를 1로 넣어서 그래프를 구성함 (연결 노드, 가중치)
distance = [INF]*(N+1)

dijkstra(X)
answer = []
for i in range(1, N+1):
    if distance[i] == K: answer.append(i)
if len(answer) == 0: print(-1)
else:
    print("\n".join(map(str, answer)))


""" bfs활용 
def bfs(start):
    answer = []
    q = deque([start]) # 시작 노드 집어넣기
    v[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not v[i]: # 아직 방문하지 않은 노드라면
                v[i] = True # 방문 표시
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K: # 해당 거리가 K와 동일하다면 해당 노드 추가
                    answer.append(i)

    if len(answer) == 0: # k번에 도달할 수 있는 노드가 아니라면
        print(-1)
    else: # 도달했다면
        answer.sort()
        print("\n".join(map(str, answer)))


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
v = [False]*(N+1)
distance = [0]*(N+1)
bfs(X)
"""