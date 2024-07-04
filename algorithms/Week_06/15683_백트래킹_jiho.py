# 감시.. 너무 어렵넹
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def cal(tlst):
    v = [[0]*(M+2) for _ in range(N+2)]
    # 모든 cctv에 대해서 처리 (좌표, type, rot)
    for i in range(CNT):
        si, sj = lst[i]    # 1~N, 1~M
        rot = tlst[i]      # 0~3
        type = arr[si][sj] # 1~5

        # type에 따른 모든 방향을 뻗어가면서 v[] 1 표시
        for dr in cctv[type]:
            dr = (dr+rot)%4
            ci, cj = si, sj
            while(True):
                ci, cj = ci+dx[dr], cj+dy[dr]
                if arr[ci][cj] == 6: break # 벽이면 멈추기
                v[ci][cj] = 1
    # 사각지대 개수 카운트
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 0 and v[i][j] ==0:
                cnt+=1
    return cnt

def dfs(n, tlst):
    global ans
    if n==CNT: # 모든 CCTV의 방향(0~3) 정하기 완료
        ans = min(ans, cal(tlst))
        return
    dfs(n+1, tlst+[0]) # 0도 회전
    dfs(n + 1, tlst + [1]) # 90도 회전
    dfs(n + 1, tlst + [2]) # 180도 회전
    dfs(n + 1, tlst + [3]) # 270도 회전

# 사무실의 세로(N), 가로(M)
N, M = map(int, input().split())
# 범위 체크 -> 맵을 벽으로 둘러싸기
arr = [[6]*(M+2)]+[[6]+list(map(int, input().split()))+[6] for _ in range(N)] +[[6]*(M+2)]

# 회전 시킬때는
# 상, 우, 하, 좌 방향을 가리킴
dx = [-1,0,1,0]  # x축
dy = [0,1,0,-1]  # y축
cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

# 모든 cctv를 90도 회전하면서 cnt==N이 될때까지 최솟값 갱신

lst = [] # cctv의 위치 저장
for i in range(N+2):
    for j in range(M+2):
        # 벽이아니고 빈칸이아니면
        if arr[i][j] != 6 and arr[i][j] != 0:
            lst.append((i, j))  # cctv번호, cctv 좌표 저장
CNT = len(lst) # cctv 개수
ans = N*M
dfs(0, []) # cctv 개수: [],  tlst
print(ans)
