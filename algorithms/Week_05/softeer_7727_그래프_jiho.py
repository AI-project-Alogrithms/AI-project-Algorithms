# 함께하는 효도 ... 다시풀기 잘 모르겠음ㅠㅠㅠㅠ
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import product

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(path, x, y, routes):
    if len(path) == 4:
        routes.append(path[:])
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in path:
            path.append((nx, ny))
            dfs(path, nx, ny, routes)
            path.pop()

def get_total_fruits(routes):
    result = 0
    visited = set()
    # print("routes: ", routes)
    for route in routes:
        # print("route: ", route)
        for x, y in route:
            if (x, y) in visited:
                print(x, y)
                return 0  # 경로가 겹치는 경우 과일을 수집하지 않음 (친구들간의 경로가 겹치는 경우)
            visited.add((x, y))
            # print("visited: ", visited)
            result += board[x][y]
    return result

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
friend_points = []
for _ in range(M):
    a, b = map(int, input().split())
    friend_points.append([a - 1, b - 1])

# 각 친구의 가능한 모든 경로 찾기
friends_routes = []
for i in range(M):
    routes = []
    dfs([friend_points[i]], friend_points[i][0], friend_points[i][1], routes)
    friends_routes.append(routes)

# 가능한 모든 경로 조합을 통해 최대 과일 수 찾기
res = 0
for comb in product(*friends_routes):
    # print(comb)
    res = max(res, get_total_fruits(comb))

print(res)