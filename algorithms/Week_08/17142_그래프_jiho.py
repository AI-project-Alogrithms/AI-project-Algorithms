# 연구소3
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(active_viruses):
    q = deque(active_viruses)
    visited = [[-1] * N for _ in range(N)]
    for (i, j) in active_viruses:
        visited[i][j] = 0

    max_time = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and arr[ni][nj] != '-':
                visited[ni][nj] = visited[ci][cj] + 1
                if arr[ni][nj] == -1:
                    max_time = max(max_time, visited[ni][nj])
                q.append((ni, nj))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1 and visited[i][j] == -1:
                return float('inf')

    return max_time


def dfs(depth, start):
    global final_ans
    if depth == M:
        current_time = bfs(selected)
        if current_time < final_ans:
            final_ans = current_time
        return

    for i in range(start, b_cnt):
        selected.append(b_loc[i])
        dfs(depth + 1, i + 1)
        selected.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

b_loc = []
empty_count = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            b_loc.append((i, j))
            arr[i][j] = '*'
        elif arr[i][j] == 1:
            arr[i][j] = '-'
        else:
            arr[i][j] = -1
            empty_count += 1

if empty_count == 0: # 빈 공간이 없다면
    print(0)
else: # 퍼질 공간이 있다면
    b_cnt = len(b_loc)
    final_ans = float('inf')
    selected = []
    dfs(0, 0)
    print(final_ans if final_ans != float('inf') else -1)