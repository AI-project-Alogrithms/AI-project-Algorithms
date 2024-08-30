# 상어 중학교
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def gravity():
    for si in range(1, N):
        for sj in range(1, N+1):
            # 전체 순회
            ci, cj = si, sj
            # 내 위치 블럭 (일반, 무지개), 아래칸이 빈칸이면 교환 (위로 반복)
            while(0<= arr[ci][cj]<=M and arr[ci+1][cj]==empty):
                arr[ci][cj], arr[ci+1][cj] = arr[ci+1][cj], arr[ci][cj]
                ci -= 1
    return
def bfs(i, j, visited):
    group = set() # 그룹 블록 위치 저장
    q = deque()
    q.append((i, j))
    visited[i][j] = True # 방문처리
    group.add((i, j))  # 블록 위치 저장
    tnum = arr[i][j]  # 타겟 블록 숫자 (색깔 지정)
    r_cnt = 0 # 무지개 블록 개수 저장
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 네방향, 미방문, 일반블록 or 무지개, 같은 색깔
            if visited[ni][nj] == False and (ni,nj) not in group and (arr[ni][nj]==tnum or arr[ni][nj]==0):
                q.append((ni,nj))
                group.add((ni,nj))  # 그룹에 추가
                if arr[ni][nj]==0: # 무지개 블록 이라면
                    r_cnt +=1
                else: # 일반블록이라면
                    visited[ni][nj] = True
    return group, r_cnt

def delete_group():
    visited = [[False] * (N+2) for _ in range(N+2)] # 방문 처리
    max_group, max_cnt = set(), 0
    for si in range(1,N+1):
        for sj in range(1,N+1):
            if visited[si][sj]==False and 0<arr[si][sj]<=M: # 미방문 일반 블록 일때
                group, r_cnt = bfs(si, sj, visited)
                # 그룹 개수가 같으면 rcnt큰값 > 행 > 열
                if len(max_group)<len(group) or ((len(max_group)==len(group)) and max_cnt<=r_cnt):
                    max_group, max_cnt = group, r_cnt

    return max_group

N, M = map(int, input().split())
# 4방향 -1로 둘러싸기 (범위 체크 필요 없음)
arr = [[-1]*(N+2)]+[[-1]+list(map(int, input().split()))+[-1] for _ in range(N)] + [[-1]*(N+2)]
empty = M+1 # 빈공간 표시
ans = 0
while True:
    # 미방문 일반 블록 기준 블록 그룹 찾기
    max_b = delete_group()
    if len(max_b)<2: # 2개 미만이면 종료
        break
    # 블록 제거
    ans += len(max_b)**2 # 점수 추가
    for x, y in max_b:
        arr[x][y] = empty  # 블록 제거
    # 중력
    gravity()
    arr = list(zip(*arr))[::-1]  # 반시계 방향 회전
    arr = [list(row) for row in arr]
    # 중력
    gravity()

print(ans)
