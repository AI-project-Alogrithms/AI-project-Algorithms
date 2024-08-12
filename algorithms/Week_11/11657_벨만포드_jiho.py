# 타임머신 - 다익스트라로 풀수 없음, 음수 순환이 존재함
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 round 반복 (모든 노드에 대해서 진행하기)
    for i in range(n):
        # 매 반복마다 모든 간선을 확인하기
        for j in range(m):
            cur, next_node, cost = egdes[j][0], egdes[j][1], egdes[j][2]
            # 현재 간선 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur]!=INF and dist[cur]+cost<dist[next_node]:
                dist[next_node] = dist[cur]+cost # 짧은 거리로 갱신
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재하는 것
                if i==n-1:
                    return True
    return False

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 모든 간선에 대한 정보 담은 리스트
egdes =[]
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용 = c
    egdes.append((a,b,c))

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우 -1
        if dist[i]==INF:
            print(-1)
        else:# # 도달할 수 있는 경우 거리 출력
            print(dist[i])
