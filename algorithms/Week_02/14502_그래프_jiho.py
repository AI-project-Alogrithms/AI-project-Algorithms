# 연구소
import sys
from sys import stdin
# sys.stdin=open("Week_02/input.txt","r")
input=sys.stdin.readline

from collections import deque, defaultdict



def bfs(tlist):
    # 3개 좌표를 1로 저장 => 벽 막기
    for i, j in tlist:
        arr[i][j] = 1
    
    # 큐 생성 및 초기화 바이러스를 큐에 넣기
    queue = deque()
    visited_q = [[0]*m for _ in range(n)]
    count = cnt-3 # 남은 0의 개수 (max값 찾을 변수)
    
    for ti, tj in virus:
        queue.append((ti, tj))
        visited_q[ti][tj] = 1
        
    # 큐에 데이터 있는 동안 한개 꺼내서 처리    
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내, 미방문, 조건 == 0
            if 0<=nx<n and 0<=ny<m and visited_q[nx][ny] == 0 and arr[nx][ny] == 0:
                visited_q[nx][ny] = 1 
                queue.append((nx,ny))
                count -= 1       
    
    # 3개 좌표를 0로 저장 => 벽 풀기
    for i, j in tlist:
        arr[i][j] = 0
    return count # 남아있는 빈칸 개수 (0의 개수)
    

# def dfs(n, tlist):
#     global ans
#     if n==3: # 종료 조건
#         # 3개 좌표 모두 선택 완료
#         ans = max(ans, bfs(tlist))
#         return
#     for j in range(cnt):
#         if v[j] == 0: 
#             v[j] = 1
#             dfs(n+1, tlist + [lst[j]])
#             v[j] = 0
        
        

# 세로, 가로, (현재 위치: 좌표x, 좌표y), 명령 개수 k
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 빈칸 위치, 바이러스 위치 저장
lst = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            lst.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))
# print(lst)
# print(virus)

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 빈칸 개수: 0으로 남은 개수
cnt = len(lst)
v = [0]*cnt
ans = 0
# n: 막을 벽 개수, []: 바이러스 퍼진 수

## 1. 백 트래킹으로 풀기: 1000ms 이상 걸림
# dfs(0, [])
# print(ans)

## 2. 루프 cnt 개중에서 3개 선택
for i in range(cnt-2):
    for j in range(i+1, cnt-1):
        for k in range(j+1, cnt): # 가능한 모든 조합 구하기
            ans = max(ans, bfs([lst[i],lst[j],lst[k]]))
print(ans)

"""
rint(arr)
arr_sum = sum(arr, [])
arr_dict = defaultdict(int)
for i in arr_sum:
    arr_dict[i] += 1
print(arr_dict)
"""