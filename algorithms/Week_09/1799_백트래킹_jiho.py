# 비숍
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def not_bi(i,j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    # ↗ ↙ ↖ ↘
    directions = [(-1, 1), (1, -1), (-1, -1), (1, 1)]

    for direction in directions:
        x, y = i, j
        while 0 <= x < N and 0 <= y < N:
            visited[x][y] = 1
            x += direction[0]
            y += direction[1]

    # print("")
    # for row in visited:
    #     print(row)

# def dfs(ncnt, lst):
#     if ncnt == 0:
#         ans = max(ans, len(lst))
#         return
#     for ci, cj in total_lst:


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0 # 최소 비숏 개수
total_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total_lst.append((i,j))
ncnt = len(total_lst) # 놓을 수 있는 전체 개수
# print(sum(map(sum, zip(*arr))))

# visited = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         not_bi(i,j)

dfs(ncnt, []) #
