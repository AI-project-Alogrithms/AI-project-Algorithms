# 지름길
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
from collections import deque
INF = int(1e9)
"""
1. 0에서 시작 -> D키로미터까지 가기: 모든 거리가 graph라고 생각하기
- D까지의 거리 -> 모든 노드
2. 최소 거리 초기화: i -> i+1 가는데 1 (cost)
3. 지름길 정보 들어오면 graph에 정보추가 
- if 지름길이 끝나는 지점 > 목표지점: continue
"""
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # dist, now
    distance[start] = 0 # 시작위치의 cost 초기화
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1] # 1씩 증가
            if cost < distance[j[0]]: # 다음 가는 거리의 cost를 업데이트 할 수 있다면
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0])) # 다음 위치 넣기
    print(distance[D])


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1, 1)) # (연결된 노드, cost)
for _ in range(N):
    start, end, cost = map(int, input().split())
    if end > D: continue
    graph[start].append((end, cost))
distance = [INF]*(D+1)
dijkstra(0) # 거리 0부터 시작
