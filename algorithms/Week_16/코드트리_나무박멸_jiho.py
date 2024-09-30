# 삼성 SW 2023 오전 기출 =>
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
ddr = [-1, -1, 1, 1]
ddc = [-1, 1, -1, 1]

n, m, K, C = map(int, input().split())

kills = [[0] * n for _ in range(n)]
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def growth():
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ai, aj = i + dr[k], j + dc[k]
                    if -1 < ai < n and -1 < aj < n and maps[ai][aj] > 0:
                        cnt += 1
                maps[i][j] += cnt


def breeding():
    breeding_maps = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                breedings_list = list()
                for k in range(4):
                    ai, aj = i + dr[k], j + dc[k]
                    if -1 < ai < n and -1 < aj < n and maps[ai][aj] == 0 and kills[ai][aj] == 0:
                        breedings_list.append((ai, aj))
                if not breedings_list:
                    continue
                tree = maps[i][j] // len(breedings_list)
                for ai, aj in breedings_list:
                    breeding_maps[ai][aj] += tree

    for i in range(n):
        for j in range(n):
            maps[i][j] += breeding_maps[i][j]


def spread_test(i, j):
    result = maps[i][j]
    if maps[i][j] == 0:
        return 0
    for k in range(4):
        for l in range(1, K + 1):
            ai, aj = i + ddr[k] * l, j + ddc[k] * l
            if not (-1 < ai < n and -1 < aj < n) or maps[ai][aj] in [0, -1]:
                break
            result += maps[ai][aj]
    return result


def spread(i, j):
    kills[i][j] = C + 1
    if maps[i][j] == 0:
        return

    maps[i][j] = 0
    kills[i][j] = C + 1
    for k in range(4):
        for l in range(1, K + 1):
            ai, aj = i + ddr[k] * l, j + ddc[k] * l
            if not (-1 < ai < n and -1 < aj < n):
                break
            if maps[ai][aj] in [0, -1]:
                kills[ai][aj] = C + 1
                break
            maps[ai][aj] = 0
            kills[ai][aj] = C + 1


def spread_spray():
    global ans
    best_tree, bi, bj = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == -1:
                continue
            tmp = spread_test(i, j)
            if tmp > best_tree:
                best_tree, bi, bj = tmp, i, j
    if not best_tree:
        return False
    spread(bi, bj)
    ans += best_tree
    return True


def kills_update():
    for i in range(n):
        for j in range(n):
            kills[i][j] = max(0, kills[i][j] - 1)


for _ in range(m):
    growth()
    breeding()
    is_tree = spread_spray()
    if not is_tree:
        break
    kills_update()

print(ans)
