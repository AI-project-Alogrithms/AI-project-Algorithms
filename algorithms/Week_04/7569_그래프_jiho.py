# 토마토
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(q):

    while(q):
        ch, cx, cy = q.popleft()
        for dh, dx,dy in ((1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            nh, nx, ny = ch+dh, cx+dx, cy+dy
            if 0<=nh<H and 0<= nx < N and 0<= ny < M and arr[nh][nx][ny] == 0 and dp[nh][nx][ny] == 0:
                # 안익은, 미방문
                dp[nh][nx][ny] = dp[ch][cx][cy] + 1 # 익은 표시
                # cnt = dp[nh][nx][ny]
                q.append((nh, nx, ny))
    # return cnt


def tomato(arr, dp):
    # 모두 익은 상태라면
    a_arr = set(sum(sum(arr, []), []))
    if len(a_arr) == 1 and list(a_arr)[0] == 1:
        return 0

    q = deque()

    # 익은 토마토가 있는 위치에서 시작
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 1 and dp[k][i][j] == 0:
                    # 익은 토마토고, 아직 dp에 저장되지 않았다면
                    q.append((k,i,j)) # 미리 큐에 담아주기, 익은 토마토 모두 동시에 시작임
                    dp[k][i][j] = 1  # 익은 표시
    bfs(q)

    # 모든 칸을 검사하여 최대 일수를 찾고, 익지 않은 토마토가 있는지 확인
    max_day = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0 and dp[k][i][j] == 0:
                    return -1
                if dp[k][i][j] > 0:
                    max_day = max(max_day, dp[k][i][j])
    return max_day-1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 익은 토마토 표시
dp = [[[0]*M for _ in range(N)] for _ in range(H)]
# day = 0
print(tomato(arr, dp))