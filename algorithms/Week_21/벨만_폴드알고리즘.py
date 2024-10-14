# 벨만 폴드 알고리즘
import sys
INF = sys.maxsize

def bf(start):
    # 시작 노드 거리 초기화
    dist[start] = 0
    # 전체 n번의 라운드 반복
    for i in range(n):
        # 매 반복마다 모든 간선 확인
        for j in range(m):
            cur, next_node, cost = edges[j]
            # 현재 간선 거쳐서 이동이 더 짧으면
            if dist[cur]!=INF and dist[next_node]>cost+dist[cur]:
                dist[next_node] = cost+dist[cur]
                if i == n-1: # 마지막 라운드에서도 값이 변화한다면
                    return True
    return False


# 노드, 간선
n, m = map(int, input().split())
# 모든 간선
edges = []
# 최단 경로 테이블
dist = [INF]*(n+1)
# 모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split()) # a-> b: cost
    edges.append((a,b,c))
# 벨만 폴드 알고리즘 수행
negative_cycle = bf(1) # 첫번째 노드부터 들어가기
if negative_cycle: # 음의 간선 순환이 있다면
    print(-1)
else: #없다면
    # 1 번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리
    for i in range(2, n+1):
        if dist[i]==INF: # 도달 불가능 곳이라면
            print(-1)
        else:
            print(dist[i])