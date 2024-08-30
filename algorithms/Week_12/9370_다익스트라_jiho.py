# 미확인도착지
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = 10**9

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for next_n, d in arr[now]:
            cost = dist+d
            if cost<distance[next_n]:
                distance[next_n] = cost # 최단 거리 저장
                # parents[next_n] = now # 이전 노드 저장
                heapq.heappush(q, (cost, next_n))
    return distance

T = int(input())
for _ in range(T):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, input().split())
        arr[a].append((b,d))
        arr[b].append((a,d))
    # print(arr)
    tlst = []
    for _ in range(t):
        tlst.append(int(input()))

    dist_s = dijkstra(s) # start 에서 다익스트라 수행
    dist_g = dijkstra(g) # g에서 다익스트라 수행
    dist_h = dijkstra(h) # h에서 다익스트라 수행

    ans = []
    for en in tlst:
        if dist_s[en] == min(dist_s[g]+dist_g[h]+dist_h[en], dist_s[h] + dist_h[g] + dist_g[en]):
            # start -> end로 가는 최단 경로가 g,h를 반드시 거쳤을때의 최단 경로와 같다면
            ans.append(en)
    ans.sort()

    print(" ".join(map(str, ans)))
