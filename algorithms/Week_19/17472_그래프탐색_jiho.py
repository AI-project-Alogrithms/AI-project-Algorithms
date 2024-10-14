# 다리만들기2
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j,num):
    q = deque()
    q.append((i,j))
    dp[i][j] = num
    while q:
        ci, cj = q.popleft()
        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and dp[ni][nj]==0:
                dp[ni][nj] = num
                q.append((ni, nj))

def find_bridge():
    for ci in range(N):
        for cj in range(M):
            if dp[ci][cj]!=0: # 섬에 도달했다면
                id = dp[ci][cj] # 해당 섬 번호 저장
                for dr in range(4): # 각 방향으로 다른 섬 만날때까지 뻗어나가기
                    ni, nj = ci+di[dr], cj+dj[dr]
                    length = 0 # 길이 계산 -> cost
                    while 0<=ni<N and 0<=nj<M: # 범위내 동안
                        if dp[ni][nj]==id: # 같은 섬을 만났다면 break
                            break
                        if dp[ni][nj]>0: # 다른 섬을 만났고, 범위내라면
                            if length>1:# 2이상 길이라면 cost가
                                bridge_lst.append((length, id, dp[ni][nj])) # cost, 정점1, 정점2
                            break
                        length+=1
                        ni += di[dr]
                        nj += dj[dr]

def find_parent(parent, x):
    # 재귀 함수 돌리기
    if parent[x] != x: # 처음 방문 하는 게 아니라면 루트 노드 찾기
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def krustal(v, bridge_lst):
    cnt = 0 # 최소 간선 개수 초기화
    ans = 0 # 최소 비용 저장
    for edge in bridge_lst:
        if cnt >= v-1:
            return ans

        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ans+= cost
            cnt+=1
    return ans



N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 다리 번호 부여
dp = [[0]*M for _ in range(N)]
num = 1
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and dp[i][j]==0:
            bfs(i,j, num)
            num+=1

# 최소 간선, 가중치 찾아서 저상
bridge_lst = []
find_bridge()

# 최소 간선 순으로 정렬
bridge_lst.sort()
# 정점의 개수: num-1/ 최소 간선의 개수 v-1
v = num-1
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i] = i

# 크루스칼 알고리즘 사용
result = krustal(v, bridge_lst)

all_connected = True
for each in parent[1:]:
    if parent[1] != parent[each]:
        all_connected = False # 모두 다 연결이 안되어 있다면 false
        break
if result==0 or all_connected==False:
    print(-1)
else:
    print(result)

