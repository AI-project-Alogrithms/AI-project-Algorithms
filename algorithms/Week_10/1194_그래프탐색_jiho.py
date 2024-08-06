# 달이 차오른다, 가자.
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(ci, cj):
    global cnt
    q = deque([(ci, cj, 0)])
    visited = [[[-1]*(1 << 6) for _ in range(M)] for _ in range(N)] # 3차원 배열로 변경
    visited[ci][cj][0] = 0 # 현재 위치 방문 표시
    while q:
        ci, cj, keys = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj][keys] == -1 and arr[ni][nj] != '#':
                if arr[ni][nj] == '.': # 그냥 지나가기
                    visited[ni][nj][keys] = visited[ci][cj][keys] + 1
                    q.append((ni, nj, keys))
                elif arr[ni][nj] == '1': # 출구라면
                    return visited[ci][cj][keys] + 1
                elif 'a' <= arr[ni][nj] <= 'f': # 키라면
                    new_keys = keys | (1 << (ord(arr[ni][nj]) - ord('a')))
                    if visited[ni][nj][new_keys] == -1: # 새 키 상태로 방문 여부 체크
                        visited[ni][nj][new_keys] = visited[ci][cj][keys] + 1
                        q.append((ni, nj, new_keys))
                elif 'A' <= arr[ni][nj] <= 'F': # 문이라면
                    if keys & (1 << (ord(arr[ni][nj]) - ord('A'))): # 해당 키가 있는지 확인
                        visited[ni][nj][keys] = visited[ci][cj][keys] + 1
                        q.append((ni, nj, keys))
    return -1

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            ci, cj = i, j # 현재 위치 받기
            arr[i][j] = '.'

cnt = bfs(ci, cj)
print(cnt)