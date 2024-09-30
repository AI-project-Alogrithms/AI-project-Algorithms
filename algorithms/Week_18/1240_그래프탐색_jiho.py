# 노드사이의 거리
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(s,end):
    q = deque()
    q.append((s, 0))
    v = [-1]*(N+1)
    v[s] = 0
    while q:
        start, d  = q.popleft()
        if start==end:
            print(v[start])
            return
        for next, dr in graph[start]:
            if v[next]==-1: # 아직 방문 전이라면
                v[next] = d+dr
                q.append((next, v[next]))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))
for _ in range(M):
    s, e = map(int, input().split())
    bfs(s,e)