# 아기상어
import sys
from sys import stdin
from collections import deque

sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def bfs(si, sj):
    # 큐, vlist 거리 저장 배열
    qu = deque()
    v = [[0] * n for _ in range(n)]  # 거리 저장 배열
    tlist = []  # 먹을 물고기 담기

    qu.append((si, sj))  # 처음 위치 넣기
    v[si][sj] = 1  # 거리 1 계산
    eat = 0  # 먹은 물고기가 있는 거리
    while qu:
        ci, cj = qu.popleft()  # 현재 위치

        # 종료 조건: eat에 적힌 거리는 모두 q에 넣었음
        if eat == v[ci][cj]:
            return tlist, eat - 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # 상하좌우로 이동하면서
            ni, nj = ci + di, cj + dj  # 다음 칸 이동
            if (
                0 <= ni < n
                and 0 <= nj < n
                and arr[ni][nj] <= sh_size
                and v[ni][nj] == 0
            ):  # 범위내, 작거나 같고, 이동 전이면
                qu.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1  # 거리 +1
                if 0 < arr[ni][nj] < sh_size:  # 상어보다 작은 물고기일때
                    # 먹기
                    tlist.append((ni, nj))
                    eat = v[ni][
                        nj
                    ]  # 현재 거리 추가 (먹는 지점 도착했을 때 거리) ex. 5가 추가됨
    # 못찾으면, 방문을 모두 끝낸 경우
    return tlist, eat - 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            ci, cj = i, j  # 초기 상어 위치 저장
            arr[i][j] = 0  # 자리 초기화

sh_size = 2  # 초기 상어 크기
cnt = ans = 0  # 먹은 수, 이동 거리


while True:
    tlist, dist = bfs(ci, cj)  # 먹었을 때의 거리와 그때 먹은 물고기가 반환됨
    if len(tlist) == 0:  # 더이상 먹을 물고기가 없는 경우
        break  # 종료
    tlist.sort(key=lambda x: (x[0], x[1]))  # 먹을 물고기를 행, 열 순으로 sort
    ci, cj = tlist[0]  # 현재 위치를 가장 먼저 먹을 물고기 위치로 변환
    arr[ci][cj] = 0  # 물고기 먹기
    cnt += 1  # 먹은 물고기 수
    ans += dist  # 이동 거리
    if sh_size == cnt:  # 자신의 크기만큼 물고기 먹었다면
        sh_size += 1
        cnt = 0


print(ans)
