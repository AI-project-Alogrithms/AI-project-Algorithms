# 운동
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# 다 익스트라로 풀어보자 => 실패
# 플로이드 위셜 문제
import heapq
INF = sys.maxsize

v, e = map(int, input().split()) # 정점, 간선
dist = [[INF]*(v+1) for _ in range(v+1)] # 최소 거리


# 그래프 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 플로이드-위셜 알고리즘 실행
for k in range(1, v+1): # 중간에 거쳐가는 노드
    for i in range(1, v+1): # 시작 노드
        for j in range(1, v+1): # 도착 노드
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# 최소 순환 경로 찾기
ans = INF
for a in range(1, v+1):
    ans = min(ans, dist[a][a])

if ans == INF:
    print(-1)
else:
    print(ans)
