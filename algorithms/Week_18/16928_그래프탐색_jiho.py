# 뱀과 사다리 게임
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(x): # 1에서 시작
    q = deque([x])
    visited[x] = 1 # 방문 표시
    while q:
        start = q.popleft()
        if start==100: # 도착했다면
            print(dp[start])
            break
        for i in range(1,7):
            # 주사위 굴리면
            next_n = start+i
            if next_n <= 100 and visited[next_n]==0: # 맵을 벗어나지 않고 아직 방문 전이라면
                # 사다리에 있다면
                if next_n in lst_n:
                    next_n = lst_n[next_n] # 사다리 타기
                # 뱀이라면
                if next_n in lst_m:
                    next_n = lst_m[next_n] # 뱀타기
                if visited[next_n]==0: # 둘다 아니고, 방문 전이라면
                    visited[next_n]=1 # 방문
                    dp[next_n] = dp[start]+1
                    q.append(next_n)
                # print(dp)

N, M = map(int, input().split())
lst_n = {}
for _ in range(N):
    a, b = map(int, input().split())
    lst_n[a] = b
lst_m = {}
for _ in range(M):
    a,b = map(int, input().split())
    lst_m[a]=b
# print(lst_n, lst_m)
# 방문 횟수
dp = [0]*101
# 방문 여부
visited = [0]*101
bfs(1)
