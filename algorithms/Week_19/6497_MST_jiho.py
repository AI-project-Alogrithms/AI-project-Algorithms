# 전력난
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def find_parent(node, x):
    # 재귀
    if node[x]!=x:
        node[x] = find_parent(node, node[x])
    return node[x]

def union_parent(node, x, y):
    x = find_parent(node, x)
    y = find_parent(node, y)
    if x<y:
        node[y] = x
    else:
        node[x] = y

while(True):
    m, n = map(int, input().split())
    if m==0 and n==0: break
    node = [0]*m
    edges = []
    all_cost = 0
    for _ in range(n):
        x,y,z = map(int, input().split())
        edges.append((z,x,y))
        all_cost+=z
    edges.sort()

    # 노드를 초기화
    for i in range(m):
        node[i]=i

    # find,
    cost = 0
    for i in range(n):
        z, x, y = edges[i]
        if find_parent(node, x) != find_parent(node, y):
            union_parent(node, x, y)
            cost+=z
    print(all_cost-cost)


