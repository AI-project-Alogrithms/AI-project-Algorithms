# 삼성 sw기출 2023 하, 왕실의 기사대결? 과 비슷
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)] # si, sj, dr
arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
exit_set = set() # 출구 정보
# for i in arr:
#     print(i)
# 출구 방향 정보,
# 북, 동, 남, 서 # 회전 (동쪽, 시계방향)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(si, sj):
    q = deque()
    v = [[0]*(C+2) for _ in range(R+4)]
    q.append((si,sj))
    v[si][sj] = 1
    max_i = 0 # -2해서 return
    while q:
        ci, cj = q.popleft()
        max_i = max(max_i, ci)
        # 네방향, 미방문, 조건: 같은값 또는 내가 출구, 상대방이 골렘
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if v[ni][nj]==0 and (arr[ci][cj]==arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj]>1)):
                q.append((ni,nj))
                v[ni][nj] = 1
    return max_i-2

num = 2 # 골렘 번호 시작
ans = 0 # 가장 아래 행 넣기
# 실제 골렘 입력 좌표/방향 따라서 남족이동 및 정렬 최대 좌표 계산 누적
for cj, dr in unit:
    ci = 1
    # 남쪽으로 최대한 이동
    while(True):
        # 남쪽으로 이동
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0: # 비어 있음
            ci +=1
        # 서쪽으로 회전하면서 아래로 한칸 이동
        elif (arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1] + arr[ci+1][cj-2] + arr[ci+2][cj-1]) == 0:
            ci+=1
            cj-=1
            dr = (dr-1)%4
        # 동쪽으로 회전하면서 아래로 한칸 이동
        elif (arr[ci-1][cj+1]+arr[ci][cj+2]+arr[ci+1][cj+1]+arr[ci+1][cj+2]+arr[ci+2][cj+1])==0:
            ci+=1
            cj+=1
            dr = (dr+1)%4
        else: break
    # 골렘 표시
    if ci<4: # 몸이 빠져 나간 것(범위 밖):
        arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)] # 초기화
        num = 2 # 골렘 초기화
        exit_set = set()  # 출구 정보 초기화
    else: # 그게 아니라면 나 표시
        # 골렘표시 + 비상구 위치 추가
        arr[ci+1][cj] = arr[ci-1][cj] = num
        arr[ci][cj-1:cj+2] = [num]*3
        num+=1
        # 골렘 표시 다했으면 정렬 옮기기
        exit_set.add((ci+dx[dr], cj+dy[dr]))
        ans += bfs(ci, cj)
print(ans)
