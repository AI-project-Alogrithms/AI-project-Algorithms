# 해킹
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = 10**9

def dijkstra(node):
    q = []
    heapq.heappush(q, (0, node)) # dist, now
    distance[node] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for next_node, s in lst[now]:
            cost = dist+s
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    filtered = [x for x in distance if x!= INF]
    print((n + 1) - distance.count(INF), max(filtered))

    return distance

T = int(input())
# 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
for _ in range(T):
    n,d,c = map(int, input().split())
    lst = [[] for _ in range(n+1)] # 컴퓨터 개수 만큼
    for _ in range(d): # 의존성
        a,b,s = map(int, input().split())
        lst[b].append((a,s))
    distance = [INF]*(n+1)
    dijkstra(c)


