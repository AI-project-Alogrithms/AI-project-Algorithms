import sys
# from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input()) # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나 더 추가
distance = [INF]*(n+1)

for _ in range(m):
    u,v,w = map(int, input().split()) # u: 출발노드, v: 도착노드, w:연겨뢴 간선의 가중치
    graph[u].append((v,w)) # 거리 정보와 도착 노드를 같이 입력함

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 우선순위, 값 형태로 들어감
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리) pop하기
        if distance[now] < dist: # 이미 입력되어 있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드
            continue
        for i in graph[now]: # 연결된 모든 노드 탐색
            if dist+i[1]<distance[i[0]]: # 기존에 입력되어 있는 값보다 크다면
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(k)
print(distance)

# 5 6
# 1
# 5 1 1
# 1 2 1
# 1 3 3
# 2 3 1
# 2 4 5
# 3 4 2
#
# [100000000.0, 0, 1, 2, 4, 100000000.0]
