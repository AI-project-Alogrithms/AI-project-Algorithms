# 구슬탈출
import sys
from sys import stdin
from collections import deque

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline


def move(i, j, dr):
    back = -1
    for cnt in range(1, 10):
        # 최대로 뻗어가서 벽을 만날때까지 진행
        ni, nj = i + dx[dr] * cnt, j + dy[dr] * cnt
        if arr[ni][nj] == "#":  # 벽을 만나면
            return cnt + back
        if arr[ni][nj] == "O":
            return cnt
        # 다른 공을 지나간 경우 벽을 만난다면 한칸 뒤로
        if arr[ni][nj] == "B" or arr[ni][nj] == "R":
            back -= 1


def dfs(n, ri, rj, bi, bj):
    global ans
    if (
        n,
        ri,
        rj,
        bi,
        bj,
    ) in v_set:  # 이미 이 시도횟수의 이 좌표 조합을 해봤음 => 가지치기
        return
    v_set.add((n, ri, rj, bi, bj))  # 이후 중복 체크 방지 위해서 방문 표시
    if ans <= n:  # 이미 ans가 최소값일때
        return
    if n > 10:  # 종료조건: 10 회 이하까지만 진행, 11회 되면 return
        return
    for dr in range(4):
        # 4방향으로 구슬 이동 [1] 각 공의 이동 거리 계산
        r_cnt = move(ri, rj, dr)  # 해당 방향으로 이동 거리 구하기
        b_cnt = move(bi, bj, dr)
        if r_cnt == 0 and b_cnt == 0:  # 아얘 이동을 안했다면
            continue
        # [2] 각 공의 이동 반영
        nri, nrj = ri + dx[dr] * r_cnt, rj + dy[dr] * r_cnt  # 이동 거리 만큼 이동 적용
        nbi, nbj = bi + dx[dr] * b_cnt, bj + dy[dr] * b_cnt

        # [3] 이동한 위치가 홀인 경우 처리 (성공/실패)
        # 구멍에 대한 처리 (빨간색만 => 성공, 파란색 => 실패)
        if arr[nbi][nbj] == "O":
            continue  # 파란색 공이 들어가면 실패
        else:
            if arr[nri][nrj] == "O":  # 빨간색 공만 홀: 성공
                ans = min(ans, n)
                return

        # [4] 둘다 홀이 아닌 경우 next로 좌표 이동
        # 현재 위치를 빈칸, 이동할 위치에 'R', 'B' 구슬 표시
        arr[ri][rj], arr[bi][bj] = ".", "."
        arr[nri][nrj], arr[nbi][nbj] = "R", "B"
        dfs(n + 1, nri, nrj, nbi, nbj)
        # 반드시 원상 복구
        arr[nri][nrj], arr[nbi][nbj] = ".", "."
        arr[ri][rj], arr[bi][bj] = "R", "B"  # b나 r 좌표가 같았다면


# n*m
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

# 좌, 우, 상, 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# red, blue, oh 위치 파악
for i in range(n):
    for j in range(m):
        if arr[i][j] == "R":
            ri, rj = i, j
        if arr[i][j] == "B":
            bi, bj = i, j
cnt = 1
ans = 11
v_set = set()  # 해당 시도회수때 빨강, 파랑 구슬 좌표가 같다면 할필요 없음
dfs(1, ri, rj, bi, bj)
if ans == 11:
    ans = -1
print(ans)

# print("")
