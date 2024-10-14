# 최소신장트리: 크루스칼 알고리즘

# 특정 원소가 속한 집한 찾기
def find_parent(parent, x):
    # 루트 노드 찾을때까지 재귀 호출
    if parent[x]!=x: # 초기화된 값이 아니면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a) # 루트 노드 찾기
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수, 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*[v+1] # 부모 테이블 초기화

# 모든 간선 담을 리스트, 최소 비용을 담을 변수
edges = []
result = 0

# 부모노드 초기화 => 자기 자신
for i in range(1, v+1):
    parent[i] = i

# 모든 간선 노드 입력 받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    # 비용 순 정렬
    edges.append((cost, a, b))

# cost 오름차순 정렬
edges.sort()

# 간선 하나씩 확인하면서 사이클이 발생하지 않았다면 집합에 포함, cost 계산
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+= cost

