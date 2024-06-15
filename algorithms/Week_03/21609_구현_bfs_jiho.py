# 상어 중학교
import sys
from sys import stdin
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
empty = m + 1  # 빈 공간 표시
# 4방향 -1로 둘러싸기 (범위 체크 필요 없음)
arr = (
    [[-1] * (n + 2)]
    + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)]
    + [[-1] * (n + 2)]
)


def bfs():

    # 미방문 일반 블럭에서 bfs 확산 (가장 큰 크기 -> 무지개...)
    v = [[0] * (n + 2) for _ in range(n + 2)]
    mx_group = set()
    mx_rcnt = 0
    for si in range(1, n + 1):
        for sj in range(1, n + 1):
            if v[si][sj] == 0 and 0 < arr[si][sj] <= m:  # 미방문 일반 블록 일때
                group = set()
                qu = deque()  # qu 생성
                qu.append((si, sj))
                group.add((si, sj))
                v[si][sj] = 1  # 방문 처리
                color = arr[si][sj]  # 컬러 지정, 시작 색깔
                r_cnt = 0

                while qu:
                    ci, cj = qu.popleft()
                    # 네방향, 미방문 일반 블록 또는 무지개, 같은 색깔
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ci + di, cj + dj
                        if (
                            v[ni][nj] == 0
                            and (ni, nj) not in group
                            and (arr[ni][nj] == color or arr[ni][nj] == 0)
                        ):
                            qu.append((ni, nj))
                            group.add((ni, nj))
                            if arr[ni][nj] == 0:  # 무지개라면
                                r_cnt += 1
                            else:  # 일반블록 표시
                                v[ni][nj] = 1
                # 그룹 개수 같으면 rcnt 큰값 > 행> 열
                if len(mx_group) < len(group) or (
                    (len(mx_group) == len(group)) and mx_rcnt <= r_cnt
                ):
                    mx_group, mx_rcnt = group, r_cnt
    return mx_group


def gravity():
    for si in range(1, n):
        for sj in range(1, n + 1):
            # 전체 순회
            ci, cj = si, sj
            # 내 위치 블럭 (일반, 무지개), 아래칸이 빈칸이면 교환 (위로 반복)
            while 0 <= arr[ci][cj] <= m and arr[ci + 1][cj] == empty:
                arr[ci][cj], arr[ci + 1][cj] = arr[ci + 1][cj], arr[ci][cj]
                ci -= 1
    return


ans = 0
while True:  # 선택한 그룹 개수가 2개 미만이면 종료
    # 1. 미방문 일반 블록 기준으로 블록 그룹 찾기
    del_group = bfs()  # 가장 큰 그룹을 찾아서 set을 보내준다.
    if len(del_group) < 2:
        break
    # 2. 선택한 블록 삭제(점수에 추가)
    ans += len(del_group) ** 2
    for ti, tj in del_group:
        arr[ti][tj] = empty

    # 3. 중력 처리
    gravity()

    # 4. 반시계 방향 90도로 회전
    arr = list(zip(*arr))[::-1]
    arr = [list(i) for i in arr]

    # 5. 중력
    gravity()
print(ans)
