# 전구를 켜라: 다익스트라 => 다시해보기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs():
    conv = {'/': 1, '\\': 0}
    straight_r = [1, -1, 0, 0]
    straight_c = [0, 0, 1, -1]
    diagonal_r = [1, -1, 1, -1]
    diagonal_c = [1, -1, -1, 1]

    def unable(_r, _c):
        return _r < 0 or _c < 0 or _r >= r or _c >= c

    r, c = map(int, input().split())
    circuit = [input().strip() for _ in range(r)]
    cost = [[[float('inf')] * 2 for _ in range(c)] for _ in range(r)]

    q = deque()
    q.append([0, 0, 0])

    if circuit[0][0] == '/':
        cost[0][0][0] = 1
    else:
        cost[0][0][0] = 0

    while q:
        cur = q.popleft()
        cr, cc, cdir = cur
        next_circuit = None
        next_cost = None
        nr = None
        nc = None

        for i in range(4):
            nr, nc = cr + straight_r[i], cc + straight_c[i]
            if unable(nr, nc):
                continue

            next_cost = cost[cr][cc][cdir]

            if cdir == conv[circuit[nr][nc]]:
                next_cost += 1
                next_circuit = (cdir + 1) % 2
            else:
                next_circuit = conv[circuit[nr][nc]]

            if next_cost >= cost[nr][nc][next_circuit]:
                continue

            cost[nr][nc][next_circuit] = next_cost
            if next_cost == cost[cr][cc][cdir]:
                q.appendleft([nr, nc, next_circuit])
            else:
                q.append([nr, nc, next_circuit])

        if not cdir:
            for i in range(2):
                nr, nc = cr + diagonal_r[i], cc + diagonal_c[i]
                if unable(nr, nc):
                    continue

                next_cost = cost[cr][cc][cdir]

                if cdir != conv[circuit[nr][nc]]:
                    next_cost += 1

                if next_cost >= cost[nr][nc][cdir]:
                    continue

                cost[nr][nc][cdir] = next_cost
                if next_cost == cost[cr][cc][cdir]:
                    q.appendleft([nr, nc, cdir])
                else:
                    q.append([nr, nc, cdir])
        else:
            for i in range(2, 4):
                nr, nc = cr + diagonal_r[i], cc + diagonal_c[i]
                if unable(nr, nc):
                    continue

                next_cost = cost[cr][cc][cdir]

                if cdir != conv[circuit[nr][nc]]:
                    next_cost += 1
                if next_cost >= cost[nr][nc][cdir]:
                    continue

                cost[nr][nc][cdir] = next_cost
                if next_cost == cost[cr][cc][cdir]:
                    q.appendleft([nr, nc, cdir])
                else:
                    q.append([nr, nc, cdir])

    ans = cost[r - 1][c - 1][0]
    if ans == float('inf'):
        print("NO SOLUTION")
    else:
        print(cost[r - 1][c - 1][0])


bfs()