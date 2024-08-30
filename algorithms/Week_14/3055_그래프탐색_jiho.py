# 탈출
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(lst):
    while q:
        ci, cj = q.popleft()
        cur = arr[ci][cj] # 현재 비버인지 물인지 판단

        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if ni < 0 or ni >= R or nj < 0 or nj >= C:  # 범위 밖이면 무시
                continue
            if dp[ni][nj] != -1:  # 이미 방문한 곳 무시
                continue
            if arr[ni][nj] == "*":  # 물 무시
                continue
            if arr[ni][nj] == "X":  # 돌 무시
                continue
            if cur == "*" and arr[ni][nj] == "D":  # 물이 비버네 가려면 무시
                continue
            if cur == 'S': # 비버이고
                if arr[ni][nj] == 'D': # 목적지라면
                    print(dp[ci][cj]+1)
                    break
                dp[ni][nj] = dp[ci][cj]+1
            arr[ni][nj] = cur # 다음 좌표 변경
            print()
            for i in arr:
                print(i)
            q.append((ni,nj))
        else:
            continue
        break
    else:
        print("KAKTUS")


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
# print(arr)
q = deque()
dp = [[-1]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D': # 굴
            ai, aj = i, j
        elif arr[i][j] == 'S': # 비버
            q.append((i,j))
            dp[i][j] = 0 # 시간 저장
        elif arr[i][j] == '*': # 물
            q.appendleft((i,j))
        # elif arr[i][j] == 'X': # 돌
        #     stone.add((i,j))


bfs(q)