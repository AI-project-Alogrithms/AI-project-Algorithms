# 백트래킹
# 메모리 초과 해결 방법: 겹치지 않게 간다 => 굳이 a,b를 나눌 필요도 없이 a가 마지막 까지 도달할때
# 가능한 모든 좌표를 지나는 경우의 수를 구하면 됨... 문제에 너무 매몰되지 말고 넓게 보자
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def dfs(n, ci, cj):
    global cnt
    if (ci, cj) == (4, 4):  # (5,5)에 도달했을 때
        if n==total:
            cnt+=1
        return

    for i in range(4):
        ni, nj = ci + di[i], cj + dj[i]
        if 0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == 0:
            arr[ni][nj] = 1
            dfs(n + 1, ni, nj)
            arr[ni][nj] = 0

K = int(input())  # 갈 수 없는 칸의 개수
arr = [[0] * 5 for _ in range(5)]
arr[0][0] = -1  # A의 시작 위치 (1,1)
arr[4][4] = 0  # B의 시작 위치 (5,5)
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = -1  # 이동할 수 없는 칸 표시

cnt = 0
total = 25 - K - 1  # A와 B가 각각 방문할 수 있는 칸 수
dfs(0, 0, 0)  # A의 경로 탐색 시작

print(cnt)
