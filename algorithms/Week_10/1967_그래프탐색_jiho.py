# 트리의 지름
"""
** 외우기
트리의 지름 -> 두번의 dfs
1) root 노드부터 시작해서 가장 먼 노드 찾기
2) 찾은 가장 먼 노드에서 시작해서 가장 먼 노드 찾아서 그 거리 구하기
"""
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(start):
    stack = [(start, 0)] # 시작위치까지 거리 0
    visited = [-1]*(n+1) # 노드 방문 여부 체크
    visited[start] = 0 # 시작위치 방문 표시
    max_d, max_n = 0, start # 거리 가장 먼저, 그때의 node
    while(stack):
        node, dist = stack.pop()
        for neighbor, w in graph[node]: # 해당 노드의 자식노드 중
            if visited[neighbor] == -1: # 미방분 노드가 있다면
                visited[neighbor] = dist+w # 방문 표시 (거리 저장)
                stack.append((neighbor, dist+w)) # 해당 노드 기준으로 돌기
                if visited[neighbor] > max_d: # 해당노드까지의 거리가 max_v보다 멀다면
                    max_d = visited[neighbor] # 거리 업데이트
                    max_n = neighbor # 해당 노드가 가장 먼 노드
    return max_n, max_d

n = int(input()) # 노드의 개수
graph = [[] for _ in range(n+1)] # 그래프
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c,w))
    graph[c].append((p,w))

# 첫번째 dfs
far_node, _ = dfs(1) # root node부터 시작
_, ans = dfs(far_node) # far_node부터 가장 먼 노드까지의 거리 구하기
print(ans)