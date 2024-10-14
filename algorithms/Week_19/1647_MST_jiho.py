# 도시 분할 계획
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def find_parent(parent, x):
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

def kruskal(v, roots):
    cnt = 0
    ans = 0
    for root in roots:
        if cnt==v:
            return ans
        c, a, b = root
        if find_parent(house, a)!=find_parent(house, b):
            union_parent(house, a, b)
            ans+=c
            cnt+=1
    return ans


# 집 개수, 길 개수
N, M = map(int, input().split())
roots = []
for _ in range(M):
    a,b,c = map(int, input().split())
    roots.append((c,a,b))
roots.sort()
house = [0]*(N+1)
for i in range(1, N+1):
    house[i] = i
print(kruskal(N-2, roots))


