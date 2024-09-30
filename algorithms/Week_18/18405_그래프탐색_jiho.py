# 경쟁적 전염
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(vlst):
    q = deque(vlst)
    ss = 0
    cnt = len(q)
    ans = 0 # 출력
    while q:
        if ss == s: # 시간 전에 큐가 안비어 있다면 강제로 멈추고 출력
            ans = arr[x - 1][y - 1]
            break
        k, ci, cj = q.popleft()
        cnt -=1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                arr[ni][nj] = k
                v[ni][nj] = 1
                q.append((k, ni, nj))
        if cnt==0:
            ss +=1
            cnt = len(q)
            # q = sorted(q, key=lambda x:x[0])
            # print()
            # for i in arr:
            #     print(i)
    if ss<s: # 시간이 되기 전에 arr다 다 찼다면 ans 넣어주기
        ans = arr[x - 1][y - 1]
    return ans


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
s, x, y = map(int, input().split())
vlst = [] # 바이러스 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            vlst.append([arr[i][j],i, j])
            v[i][j] = 1 # 방문 표시

# 크기가 작은 순서대로
vlst.sort(key=lambda x: x[0])
print(bfs(vlst))


