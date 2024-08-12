# 벽 부수고 이동하기 4
# 메모리제이션 이용하기가 중요함.. 어려웠음ㅜ
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque, defaultdict

# 그룹 표시 및 그룹 내 0의 개수 반환
def bfs(i,j):
    q = deque()
    q.append((i,j))
    glst[i][j] = gnum # 해당 그룹임을 표시
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni<N and 0<= nj < M and visited[ni][nj]==0 and arr[ni][nj]==0:
                visited[ni][nj] = 1
                glst[ni][nj] = gnum # 해당 그룹 표시
                cnt +=1
                q.append((ni,nj))
    return cnt # 그룹 개수 반환


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)] # 주어진 배열이자 최종 답으로 할 것
visited = [[0]*M for _ in range(N)] # 방문 표시
glst = [[0]*M for _ in range(N)] # 그룹 표시
gdict = defaultdict(int)
gnum = 1 # 그룹 넘버

# 그룹 나누기 및 그룹 내 0의 개수 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0: # 0이고, 아직 미방문이면
            visited[i][j] = 1 # 방문 표시
            cnt = bfs(i,j) # 그룹 표시 및 그룹 내 0의 개수 반환
            gdict[gnum] = cnt
            gnum +=1
# for i in glst:
#     print(i)
# print(gdict)

# 벽인거 찾아서 사분면 돌면서 해당 그룹이면 set으로 추가하기 (중복 방지)
for ci in range(N):
    for cj in range(M):
        if arr[ci][cj] == 1: # 벽이면
            addlst = set()
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj = ci+di, cj+dj
                if 0<= ni < N and 0<= nj < M:
                    addlst.add(glst[ni][nj]) # 그룹 번호 추가
            for add in addlst:
                arr[ci][cj] += gdict[add]
                arr[ci][cj] %= 10

for i in arr:
    print("".join(map(str, i)))