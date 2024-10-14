# 최소 스패닝 트리
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def find_parent(parent, x):
    # 재귀 호출
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(v, edges):
    ans = 0  # 최소 비용
    cnt = 0  # 간선의 최소 개수: 노드개수 -1
    for edge in edges:
        if cnt >= v - 1:
            return ans

        c, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ans += c
            cnt += 1
    return ans

v, e = map(int, input().split())
parent = [0]*(v+1) # 부모노드
# 노드 초기화 자기 자신
for i in range(1,v+1):
    parent[i] = i
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

# 크루스칼 알고리즘
print(kruskal(v, edges))

