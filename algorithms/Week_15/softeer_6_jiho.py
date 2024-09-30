# 출퇴근길
## 참고 링크 https://velog.io/@wp29dud/%EC%B6%9C%ED%87%B4%EA%B7%BC%EA%B8%B8-%ED%92%80%EC%96%B4-%EB%B4%84
# 문제 핵심: 역방향 탐색

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node, graph, visited):  # 노드, 돌 그래프, 방문 여부
    if visited[node] == 1:  # 방문 했다면
        return
    visited[node] = 1  # 방문 안했다면 방문 표시
    for next in graph[node]:
        dfs(next, graph, visited)
    return


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 역 간선 그래프 이용하기..
graphR = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graphR[y].append(x)
# print(graph)
# print(graphR)
# 집, 회사
s, t = map(int, input().split())

fromS = [0] * (n + 1)
fromS[t] = 1
dfs(s, graph, fromS)

fromT = [0] * (n + 1)
fromT[s] = 1
dfs(t, graph, fromT)

toS = [0] * (n + 1)
dfs(s, graphR, toS)

toT = [0] * (n + 1)
dfs(t, graphR, toT)

cnt = 0
for i in range(1, n + 1):
    if fromS[i] == fromT[i] == toS[i] == toT[i] == 1:
        cnt += 1
print(cnt - 2)
