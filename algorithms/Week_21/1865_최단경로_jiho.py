# 웜홀 => 음의 간선 포함 => 벨만 폴드
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

def bf(start):
    dist[start] = 0 # 시작 시간 0
    # 모든 노드에 대해서 최단 거리 구하기
    for i in range(N):
        # 매 반복마다 전체 간선 확인
        for j in range(len(edges)):
            s, e, t = edges[j]
            if dist[e]>dist[s]+t:
                dist[e] = dist[s]+t
                if i==N-1:
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split()) # 지점의 수, 도로의 개수, 웜홀의 개수
    dist = [INF]*(N+1) # 최단 경로 저장
    edges = [] # 도로 및 웜홀 저장
    for _ in range(M): # 양방향
        s,e,t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(W): # 웜홀은 한방향
        s, e, t = map(int, input().split())
        edges.append((s,e,-t))

    negative_path = bf(1)
    if negative_path:
        print("YES")
    else:
        print("NO")

