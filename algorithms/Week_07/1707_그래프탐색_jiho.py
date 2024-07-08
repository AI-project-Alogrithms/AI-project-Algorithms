# 이분 그래프
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(start, group):
    q = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정
    while(q):
        node = q.popleft()
        for i in arr[node]: # 해당 정점 돌동안
            if visited[i] == 0: # 아직 미방문 노드라면
                q.append(i)
                visited[i] = -1 * visited[node] # 다른 그룹으로 두기
            elif visited[i] == visited[node]: # 이미 방문, 부모와 같은 그룹이라면
                return False
    return True



T = int(input())
for _ in range(T):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    visited = [0]*(v+1) # 방문한 정점 체크

    for _ in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            result = bfs(i, 1)
            if not result: # false를 return 하면 바로 멈추고 출력
                break
    print('YES' if result else 'NO')

