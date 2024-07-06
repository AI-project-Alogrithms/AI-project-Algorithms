import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

# n개의 노드 순회하면서 해당 노드를 시작으로 bfs 진행
def bfs(start):
    q = deque([start])
    visited = [0]*n
    while(q):
        node = q.popleft()
        # 현재 노드와 연결된 노드 확인
        for i in adj_lst[node]:
            # 현재 노드와 연결된 노드를 아직 방문하기 전이라면 방문 진행
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    print(*visited)


n = int(input())
adj_lst = [[] for _ in range(n)]
# 인접 리스트로 변형
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            adj_lst[i].append(j)
for i in range(n):
    bfs(i) # 각 정점마다 도는지 확인