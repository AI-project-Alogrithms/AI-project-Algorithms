# 청소년 상어
import sys
from sys import stdin
from collections import deque
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


# 0~7
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,-1,-1,-1,0,1,1,1]

def find(idx, v):
    for i in range(4):
        for j in range(4):
            if v[i][j][0] == idx:
                return i,j,v[i][j][1]

def dfs(si, sj, sd, sm, v):
    global ans
    # [0] 정답 갱신: 종료 조건 n 관련 등 명확하지 않음
    ans = max(ans, sm)

    # [1] 물고기 이동 (1~16): 기준 v[] 있는 좌표
    # 먼저 i,j 좌표 검색하기
    for idx in range(1,17):
        ci, cj, dr = find(idx, v)
        # 물고기가 있는 경우
        if dr == -1: continue # 물고기가 없는 경우 skip
        for j in range(8):
            # 현재 방향부터 총 8뱡항
            td = (dr+j)%8
            ni, nj = ci+di[td], cj+dj[td]
            if 0<=ni<4 and 0<=nj<4 and (ni, nj) != (si, sj):
                v[ci][cj][1]=td # 방향 적용 후 교환
                v[ci][cj], v[ni][nj] = v[ni][nj], v[ci][cj]
                break
    # [2] 상어의 이동 (1칸~3칸, 범위내, 빈칸이 아니면)
    for mul in range(1,4):
        ni, nj = si+di[sd]*mul, sj+dj[sd]*mul
        if 0<= ni<4 and 0<= nj<4 and v[ni][nj][1] != -1:
            fn, fd = v[ni][nj]
            v[ni][nj][1] = -1 # 물고기 먹기
            nv = [[x[:] for x in lst] for lst in v] # 물고기 이동 원상복구 복잡하므로 차라리 복사해서 넣기
            dfs(ni, nj, fd, sm+fn, nv)
            v[ni][nj][1] = fd # 다음칸으로 뻗어가기 원상복구


# 물고기 입력, v[] 초기화
v = [[[0]*2 for _ in range(4)] for _ in range(4)]
print(v)
for i in range(4):
    fish_lst = list(map(int, input().split()))
    for j in range(4):
        v[i][j] = [fish_lst[j*2], fish_lst[j*2+1]-1]
print(v)
# 상어가 초기위치 물고기 먹음
ans = 0
fn, fd = v[0][0] # 물고기 먹는 처리 주의 ([1] =- 1)
v[0][0][1] = -1  # (0,0) 위치 물고기 먹기 처리
dfs(0,0,fd,fn,v) # 상어 위치, 방향, 초기 점수, v[] 전달
print(ans)