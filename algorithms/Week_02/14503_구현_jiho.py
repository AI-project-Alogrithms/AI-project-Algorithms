# 로봇 청소기
import sys
from sys import stdin

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline

from collections import deque, defaultdict


def bfs(cx, cy, d):
    global all_clear
    queue = deque([])
    queue.append((cx, cy, d))
    while queue:
        cx, cy, d = queue.popleft()
        if room[cx][cy] == 0:  # 청소가 안된 상태라면 청소
            room[cx][cy] = 2
            all_clear += 1

        clear = 0
        cnt = 0
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 1:  # 벽이 아니라면
                cnt += 1  # 갈수 있는 방향 수
                if room[nx][ny] == 2:  # 현재 위치에서 네방향 청소상태 확인
                    clear += 1
        if clear == cnt:  # 모두 청소된 상태라면
            nx, ny = cx + bx[d], cy + by[d]  # 후진
            if (
                0 <= nx < n and 0 <= ny < m and room[nx][ny] != 1
            ):  # 후진할 수 있다면 큐에 넣기
                queue.append((nx, ny, d))
            else:
                # 후진할 수 없다면 정지
                break
        elif clear < cnt:  # 청소가 안된 부분이 있다면
            for i in range(4):
                d = rotate[d]  # 90도 회전
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:  # 전친
                    queue.append((nx, ny, d))
                    break
                # else:
                #     rd = rotate[rd]


n, m = map(int, input().split())
# (r,c), 방향 d
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# print(room)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 후진
# 남, 서, 북, 동
bx = [1, 0, -1, 0]
by = [0, -1, 0, 1]

# 90도 회전
# 서, 북, 동, 남
rotate = [3, 0, 1, 2]
# rx = [0, -1, 0, 1]
# ry = [-1, 0, 1, 0]

all_clear = 0
bfs(r, c, d)
print(all_clear)
