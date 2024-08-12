# 서강그라운드
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)

# 각 노드별 최단 경로 구하기
def dijkstra(start):
    distlst = [INF] * (n + 1)  # 최단거리초기화
    q = []
    heapq.heappush(q, (0, start)) # dist, now
    distlst[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distlst[now]: continue
        for j in arr[now]:
            cost = dist + j[1]
            if cost<distlst[j[0]]:
                distlst[j[0]] = cost # 최단거리 업데이트
                heapq.heappush(q, (cost, j[0]))
    return distlst



n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split())) # 각 지역의 아이템 수
# print(item)
arr = [[] for _ in range(n+1)] # 간선 저장

for _ in range(r):
    a,b,l = map(int, input().split())
    arr[a].append((b,l))
    arr[b].append((a,l))

ans = 0 # 최대 아이템 개수
for now in range(1, n+1):
    item_num = 0
    dist = dijkstra(now)
    # print("dist: ", dist)
    for idx, cost in enumerate(dist):
        if cost <= m:
            item_num+=item[idx]
    # print("item_num: ", item_num)
    ans = max(ans, item_num)
print(ans)