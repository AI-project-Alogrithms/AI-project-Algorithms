# 플로이드 => 다익스트라로 품
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
import heapq

def dijkstra(node):
    q = []
    heapq.heappush(q, (0, node))
    v = [INF]*(n+1)
    v[node] = 0 # 자기자신으로 가는거 0
    while q:
        dist, now = heapq.heappop(q)
        if dist>v[now]: continue
        for nnode, ndist in arr[now]:
            cost = dist+ndist
            if cost<v[nnode]:
                v[nnode] = cost
                heapq.heappush(q, (cost, nnode))
    return v[1:]


n = int(input()) # n개의 도시
m = int(input()) # m개의 버스

arr = [[] for _ in range(n+1)] # 버스 노선 표

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c)) # (도착도시, cost)
# for i in arr:
#     print(i)

for i in range(1,n+1):
    visited = dijkstra(i)
    for i in visited:
        if i==INF:
            print(0, end=" ")
        else:
            print(i, end=" ")
    print()
    # print(" ".join(map(str, visited)))


