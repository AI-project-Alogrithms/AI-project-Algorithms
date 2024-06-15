# 마법사 상어와 파이어스톰
import sys
from sys import stdin
from collections import deque

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline

n, q = map(int, input().split())
N = 2**n
arr = (
    [[0] * (N + 2)]
    + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    + [[0] * (N + 2)]
)
lst = list(map(int, input().split()))

# print(arr)
# print(lst)
for L in lst:  # Q번 시전할 부분 격자 크기 순차 처리
    L = 2**L  # 부분 격자 한변 크기 저장
    # [1] 부분 격자를 시계방향으로 90도 회전
    new = [[0] * (N + 2) for _ in range(N + 2)]
    for si in range(1, N + 1, L):
        for sj in range(1, N + 1, L):  # 가능한 모든 기준 위치 만들기 (좌측 상단)
            for i in range(L):
                for j in range(L):
                    new[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
    arr = new
    # [2] 네방향 0이 2개 이상이면, 얼음 -1
    new = [x[:] for x in arr]  # 따로 빼서 deepcopy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 전체 순회
            if arr[i][j] == 0:
                continue  # 얼음이 아니면 skip
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if arr[ni][nj] == 0:  # 얼음이 아니면
                    cnt += 1
                    if cnt >= 2:
                        new[i][j] -= 1  # 얼음 -1
                        break  # 다음 위치로
    arr = new


def bfs(si, sj):
    queue = deque([])
    queue.append((si, sj))
    v[si][sj] = 1  # q에 초기 데이터 삽입 v 방문 표시
    max_sum = 1
    while queue:
        si, sj = queue.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):  # 네방향 미방문 얼음이면
            ni, nj = si + di, sj + dj
            if arr[ni][nj] > 0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                max_sum += 1
                queue.append((ni, nj))
    return max_sum


# 정답 처리: 남은 얼음 덩어리중 가장 큰 크기
v = [[0] * (N + 2) for _ in range(N + 2)]
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if v[i][j] == 0 and arr[i][j] > 0:  # 미방문 얼음이면
            ans = max(ans, bfs(i, j))

print(sum(map(sum, arr)))
print(ans)
