# 불
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(ji_fire):
    q = deque()

    # 지훈이의 초기 위치
    ci, cj = ji_fire[0]
    v[ci][cj] = 0  # 지훈이의 위치를 0으로 설정
    q.append((ci, cj, "j"))  # 지훈이의 위치를 큐에 추가

    # 불의 초기 위치
    if len(ji_fire) > 1:
        for fi, fj in ji_fire[1:]:
            q.append((fi, fj, "f"))  # 불의 위치를 큐에 추가
            v[fi][fj] = '#'  # 불의 위치를 벽으로 설정

    while q:
        ci, cj, case = q.popleft()

        # 지훈이가 탈출할 수 있는지 확인
        if case == 'j' and (ci == 0 or ci == r - 1 or cj == 0 or cj == c - 1):
            if v[ci][cj] == '#':  # 불이 있는 곳이면 패스
                continue
            return v[ci][cj] + 1  # 지훈이 탈출 시 시간 반환

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < r and 0 <= nj < c:
                if graph[ni][nj] == "." and v[ni][nj] == -1:  # 불이 퍼질 수 있는 곳
                    if case == "f":
                        v[ni][nj] = '#'
                        q.append((ni, nj, "f"))
                    elif case == "j" and v[ci][cj] != '#':  # 지훈이가 이동할 수 있는 곳
                        v[ni][nj] = v[ci][cj] + 1
                        q.append((ni, nj, "j"))

    return "IMPOSSIBLE"

# 입력 처리 부분
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
v = [[-1]*c for _ in range(r)]  # 방문 여부를 체크하기 위한 2차원 리스트
ji_fire = []

# 지훈이와 불의 초기 위치를 추출
for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":  # 지훈이의 위치
            ji_fire.append((i, j))
        if graph[i][j] == "F":  # 불의 위치
            ji_fire.append((i, j))

print(bfs(ji_fire))


